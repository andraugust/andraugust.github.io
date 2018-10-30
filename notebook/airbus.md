---
layout: page
title: "Airbus"
permalink: /airbus/
---


<br />
<h2><center>Kaggle Ship Detection Challenge</center></h2>

The Kaggle Ship Detection Challenge (sponsored by Airbus) provides satellite images of the ocean and ground-truth masks of ships in each image.  The objective is to create a model that accurately localizes ships in a set of testing images.  This post walks through my solution to the challenge.

## Data Exploration
Getting the data:
```bash
$ mkdir Airbus
$ cd Airbus
$ kaggle competitions download -c airbus-ship-detection
$ unzip ./train_v2.zip -d ./data/train_v2/
$ unzip ./test_v2.zip -d ./data/test_v2/
$ unzip ./train_ship_segmentations_v2.csv.zip -d ./data/
```

Check if any images are corrupt:
```bash
$ find ./data/test_v2/ -name "*.jpg" | xargs jpeginfo -c | grep "WARNING"
$ find ./data/train_v2/ -name "*.jpg" | xargs jpeginfo -c | grep "WARNING"
>>> ./data/train_v2/6384c3e78.jpg  768 x 768  24bit JFIF  N   98304  Premature end of JPEG file  [WARNING]
```

One of the images is corrupt, but it's a training image, so we don't need to predict on it, so we can delete it.
```bash
$ rm ./data/train_v2/6384c3e78.jpg
```

How many images are there?
```bash
$ find ./data/train_v2/ -name "*.jpg" | wc -l  # train
>>> 192555
$ find ./data/test_v2/ -name "*.jpg" | wc -l  # test
>>> 15606
```
How many train images do/don't have ships?
```python
import numpy as np
import pandas as pd

# Get images that have ships
df = pd.read_csv('./data/train_ship_segmentations_v2.csv')
has_ship = [isinstance(_, str) for _ in df['EncodedPixels']]  # true if has ship
df_with_ships = df.loc[has_ship]

print('n with ships:', np.sum(has_ship))
print('n without ships:', len(has_ship)-np.sum(has_ship))
```
The result is mostly no ships: 150,000 without and 81,723 with.

What do images with ships look like?
```python
from skimage.io import imread
import utils
import matplotlib.pyplot as plt
plt.switch_backend('agg')

# Get images that have ships
df = pd.read_csv('./data/train_ship_segmentations_v2.csv')
has_ship = [isinstance(_, str) for _ in df['EncodedPixels']]  # true if has ship
df_with_ships = df.loc[has_ship]

# Accumulate rles that belong to the same image
rle_dict = {}
for _, im_id, rle in df_with_ships.itertuples():
    if im_id in rle_dict:
        rle_dict[im_id].append(rle)
    else:
        rle_dict[im_id] = [rle]

# Plot
n_plots = 6
plt_count = 0
for im_id, rles in rle_dict.items():
    plt_count += 1
    plt.subplot(2, n_plots, plt_count)
    plt.imshow(imread('./data/train_v2/' + im_id))
    plt.gca().set_xticks([])
    plt.gca().set_yticks([])
    plt.subplot(2, n_plots, plt_count+n_plots)
    plt.imshow(utils.rles2mask(rles))
    plt.gca().set_xticks([])
    plt.gca().set_yticks([])
    if plt_count == n_plots:
        plt.subplots_adjust(wspace=0, hspace=0)
        plt.savefig('./figures/train_images_masks.png', dpi=500)
        break
```
<br />
<center><a href="../airbus/train_image_masks.png"><img src="../airbus/train_image_masks.png"></a></center>
<br />

Some ships are large and easy to distinguish, like the first column, but others are small and hard to detect, like the last column.  Some ships are _very_ close together, making them hard to separate, even when zoomed in:
<br />
<center><img src="../airbus/train_image_masks_closeup.png"></center>
<br />

Some images have one ship while others have multiple.  What's the distribution over ships per image, given there are ships?
```python
ship_counts = [len(item[1]) for item in rle_dict.items()]
max_ships = max(ship_counts)
plt.hist(ship_counts, bins=range(max_ships))
plt.xticks(range(max_ships))
plt.xlim((1,max_ships))
plt.xlabel('Number of Ships')
plt.ylabel('Number of Images')
plt.savefig('./figures/ship_count_distribution.png')
```
<br />
<center><img src="../airbus/ship_count_distribution.png"></center>
<br />

Most images have only one ship, and nearly all have less than three.

What surface area do ships cover?
```python
areas = []
for im_id, rles in rle_dict.items():
    for rle in rles:
        mask = utils.rle2mask(rle)
        areas.append(np.sum(mask))

min_area = min(areas)
max_area = max(areas)
print(min_area)
print(max_area)
plt.hist(areas, bins=range(min_area,max_area,200))
plt.xticks(range(0,26000,5000))
plt.xlim((min_area,max_area))
plt.xlabel('Ship Area')
plt.ylabel('Count')
plt.savefig('./figures/ship_areas.png')
```
<br />
<center><img src="../airbus/ship_areas.png"></center>
<br />

The smallest is tiny, only 2 pixels.  The largest is 25,904 pixels, about 4% of the image.  Most are in the hundreds range.  Here's a zoom-in:
<br />
<center><img src="../airbus/ship_areas_zoom.png"></center>
<br />

## Modeling
To model, we'll train a binary classifier to indicate if an image has at least one ship or not, then we'll train a localization model on only images with ships.

Before implementing the binary classifier, we're going to cut images into square quarters.  This is so that the localization model can train on images that have a more balanced pixel-wise class distributions, i.e., the ratio of no-ship pixels to ship pixels will be closer to 0.5 (though it'll still be fairly far off).  Also, by cutting images into quarters, batch sizes of 32 will fit in my GPU memory and it won't be necessary to down-sample images, which would cause resolution loss.

A concern about quartering images, however, is that ships will get split across quarters, leaving behind a sliver that might be hard to detect.  Let's see how many ships get split:

```python
rles = df['EncodedPixels'].tolist()
rles = [_ for _ in rles if isinstance(_,str)]   # remove empty masks

# Convert to mask, check if in multiple sectors
n_crossing = 0
for rle in tqdm(rles):
    mask = utils.rle2mask(rle)
    # Cut into quarters
    sectors = [
        mask[0:384, 0:384],
        mask[0:384, 384:],
        mask[384:, 0:384],
        mask[384:, 384:],
    ]

    in_sector = [np.sum(sector)>0 for sector in sectors]

    if np.sum(in_sector) > 1:
        n_crossing += 1

print(n_crossing)
```

The result is 10,045, so about 12% of ships get split.  That's more than we'd like, but I think the trade-off will be worth it, so we'll do the cutting anyway and check later to see if split ships are indeed harder to detect.

Quartering images:

```python
# quartify.py
from multiprocessing import Pool
from skimage.io import imread, imsave

imgs_root = sys.argv[0]
out_root = sys.argv[1]
paths = glob(imgs_root+'**/*.jpg', recursive=True)
df = read_csv('./data/train_ship_segmentations_v2.csv')

def make_quarters(path):
    im_id = path.split('/')[-1]
    id_no_jpg = im_id.split('.')[0]
    rles = df.loc[df['ImageId']==im_id, 'EncodedPixels'].tolist()
    # Get mask
    mask = utils.rles2mask(rles)
    # Quarter masks
    mask_quarters = [
        mask[0:384, 0:384],
        mask[0:384, 384:],
        mask[384:, 0:384],
        mask[384:, 384:]
    ]
    # Binary label for each quarter
    mask_labels = [np.sum(_)>0 for _ in mask_quarters]
    mask_labels = [int(_) for _ in mask_labels]
    # Load image
    im = imread(path)
    im_quarters = [
        im[0:384, 0:384, :],
        im[0:384, 384:, :],
        im[384:, 0:384, :],
        im[384:, 384:, :]
    ]
    # Save image in <root>/<class>/<id>/<id>_<quarter>.jpg
    for i, im_quarter in enumerate(im_quarters):
        save_path = '%s%i/%s/%s_%i.jpg' % (out_root, mask_labels[i], id_no_jpg, id_no_jpg, i)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        imsave(save_path, im_quarter, plugin='pil', quality=100)

pool = Pool(4)
for _ in tqdm(pool.imap_unordered(make_quarters, paths), total=len(paths)):
    pass
pool.close()
```
```bash
$ python -W ignore quartify.py ./data/train_v2/ ./data/quartered/train_v2/    # suppress annoying skimage warnings
```

The train set now has 706,997 negative instances and 63,223 positive instances.  We'll balance the set by keeping 63,223 negative instances and ignore the rest.  The assumption is that 706,997 negative instances goes beyond the point of diminishing return for sample size and having fewer samples will accelerate architecture testing.

### The Binary Model

The set is split 0.75/0.25 train/val, and train images are rotated arbitrarily by 0, 90, 180, or 270 degrees on each epoch with the hope that this will make the model more invariant to rotations.

After playing with several architectures, I found the best to be an Xception model with ImageNet weights, global max-pooling applied to the last convolutional output, and one sigmoid node on the end to represent probability of ship.  The first 50 layers of the network were frozen to minimize training time.

After the third epoch the validation accuracy reaches a maximum of 0.89 and the f-score reaches a maximum of 0.88.  The confusion matrix is

```bash
[[15529   277]
 [ 3177 12629]]
```

where rows are ground-truth and columns are predicted.  We see that there are many more false positives than false negatives.  This is a good thing because the real data, i.e., the testing data, is expected to have many more negative samples than what's used in this validation set, so the testing accuracy should be significantly higher than what's shown here.  In fact, we can approximate the testing accuracy.  If the testing data has the same bias as the training data (0 = 92%, 1 = 8%), and the tp/tn/fp/fn rates are the same between validation and testing, then the testing accuracy will be about 97%. Not bad.

Let's look at some validation misclassifications:
<br />
<center><a href="../airbus/false_negatives.png"><img src="../airbus/false_negatives.png"></a></center>
<br />
<center><a href="../airbus/false_positives.png"><img src="../airbus/false_positives.png"></a></center>
<br />

False negatives mostly occur when ships are either split, occluded by clouds, or really small; false positives mostly occur when there's a rectangular object in the image or there's a _mislabeled_ image.  _Several training images are mislabelled_.  For example, the bottom right image clearly has a ship, but the ground-truth says it's not there.  We just have to deal with that.

### The Localization Model

The localization model we'll use is a Unet with the same architecture as in the original Unet [paper](https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/).

We train directly on the 384x384 quarters using a 0.75/0.25 train/val split.  The optimizer is Adam with learning-rate 0.0001, batch size is 6, and the loss is pixel-wise binary cross entropy.  Here's the validation loss over epochs:
<br />
<center><img src="../airbus/unet_loss.png"></center>
<br />

And here are some validation predictions after each epoch, click to enlarge:
<br />
<center><a href="../airbus/unet_predictions.png"><img src="../airbus/unet_predictions.png"></a></center>
<br />

The results are pretty impressive.  After just the first epoch the model localizes ships, and after the second/third epoch it distinguishes ships from their wakes and land.  What's really impressive is that predictions look like genuine _bounding boxes_, even though ships themselves aren't rectangular.  The model even localizes ship fragments on the edges of images, which is what we were worried it would have trouble with when we did the quartering.

Let's see where Unet performed poorly.  These validation samples have the biggest loss:
<br />
<center><a href="../airbus/unet_errors.png"><img src="../airbus/unet_errors.png"></a></center>
<br />

Evidently, docked ships are hardest to detect, they just look like a continuation of the land, especially the yachts, which, in some sense, are.  The second to last column has what appear to be oil rigs that were misclassified.  The predictions, though, are very ir-rectangular compared to real ships, and we can try to use this information to our advantage when we do processing triage.

### The Objective Function

The objective function used by Kaggle is somewhat convoluted.  For each image, an intersection-over-union is computed between any predictions and ground-truths that might exist.  The IoU is then thresholded over a set of values to determine if the prediction will be a TP.  Then, f2 score is calculated and averaged for each threshold.  Then, that average f2 score is averaged over all images, and that's your prediction score.  Note that bounding-boxes aren't used as predictions, but instead run-length encoded masks, so really they can look like anything.  It isn't entirely clear if a single mask can be TP for multiple ships, or how predictions are assigned to ground-truths when there are multiple predictions and ground-truths per image, but more info on scoring is [here](https://www.kaggle.com/c/airbus-ship-detection#evaluation).

To get a sense of where to threshold Unet predictions, let's loop over thresholds and look at average IoUs on the validation set (with error bars of 1 std dev on each side):
<br />
<center><a href="../airbus/iou_v_thresh.png"><img src="../airbus/iou_v_thresh.png"></a></center>
<br />
We'll use 0.4 as a threshold.


### Testing

Let's spot-check some test predictions.

### Post-processing

Submissions
- 2unets thresh 0.4, 2bin, area thresh 40: 0.692
- 2unets thresh 0.4, area thresh 60: 0.687
- 2unets thresh 0.4, area thresh 40: 0.687
- 2unets thresh 0.4, area thresh 20: 0.686
- unet thresh 0.4, area thresh 40: 0.680
- blank: 0.520


- threshold unet, ship area 40, box_area 0.2: 0.680
- threshold unet, ship area 40, box_area 0.4: 0.679
- threshold unet, ship area 20: 0.680
- threshold unet, ship area 20, box_area 0.2: 0.680
- threshold unet, ship area 100: 0.679
- threshold unet, mode filter
- threshold unet, mode filter, bbox
- threshold at 0.5, bbox, delete small ones, delete big ones, delete weird ones

```python
from keras import backend as K
from keras.models import Model, Sequential
from keras.layers import Conv2D, Input, MaxPooling2D, Dropout, UpSampling2D, MaxPool2D, Flatten, Dense
from keras.optimizers import Adam
from keras.layers.merge import concatenate

def unet(pretrained_weights=None, input_size=(256, 256, 3), kernel_sz=3):
    inputs = Input(input_size)
    conv1 = Conv2D(64, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(inputs)
    conv1 = Conv2D(64, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
    conv2 = Conv2D(128, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(pool1)
    conv2 = Conv2D(128, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(conv2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
    conv3 = Conv2D(256, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(pool2)
    conv3 = Conv2D(256, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(conv3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)
    conv4 = Conv2D(512, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(pool3)
    conv4 = Conv2D(512, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(conv4)
    drop4 = Dropout(0.5)(conv4)
    pool4 = MaxPooling2D(pool_size=(2, 2))(drop4)

    conv5 = Conv2D(1024, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(pool4)
    conv5 = Conv2D(1024, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(conv5)
    drop5 = Dropout(0.5)(conv5)

    up6 = Conv2D(512, 2, activation='relu', padding='same', kernel_initializer='he_normal')(UpSampling2D(size=(2, 2))(drop5))
    merge6 = concatenate([drop4, up6], axis=3)
    conv6 = Conv2D(512, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(merge6)
    conv6 = Conv2D(512, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(conv6)

    up7 = Conv2D(256, 2, activation='relu', padding='same', kernel_initializer='he_normal')(UpSampling2D(size=(2, 2))(conv6))
    merge7 = concatenate([conv3, up7], axis=3)
    conv7 = Conv2D(256, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(merge7)
    conv7 = Conv2D(256, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(conv7)

    up8 = Conv2D(128, 2, activation='relu', padding='same', kernel_initializer='he_normal')(UpSampling2D(size=(2, 2))(conv7))
    merge8 = concatenate([conv2, up8], axis=3)
    conv8 = Conv2D(128, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(merge8)
    conv8 = Conv2D(128, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(conv8)

    up9 = Conv2D(64, 2, activation='relu', padding='same', kernel_initializer='he_normal')(UpSampling2D(size=(2, 2))(conv8))
    merge9 = concatenate([conv1, up9], axis=3)
    conv9 = Conv2D(64, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(merge9)
    conv9 = Conv2D(64, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(conv9)
    conv9 = Conv2D(2, kernel_sz, activation='relu', padding='same', kernel_initializer='he_normal')(conv9)
    conv10 = Conv2D(1, 1, activation='sigmoid')(conv9)

    model = Model(inputs=inputs, outputs=conv10)

    # model.compile(optimizer=Adam(lr=1e-4), loss='binary_crossentropy', metrics=['accuracy'])
    model.compile(optimizer=Adam(lr=1e-4), loss=[focal_loss], metrics=['accuracy'])

    if pretrained_weights:
        model.load_weights(pretrained_weights)

    return model

```

### Misc notes
- Unet took about 48 hours to train on my 8GB GTX1080.  The maximum energy usage of the GPU is around 180W, and the CPU is probably (?) using about the same; local residential electricity cost is 8.5c/kWh, so the Unet took about 1.50$ cents to train---take that aws!
