---
layout: page
title: "Airbus"
permalink: /airbus/
---


The Kaggle Ship Detection Challenge sponsored by Airbus provides a set of satellite images of the ocean with corresponding ground-truth masks identifying the locations of ship in each image.  The objective is to create a model that accurately masks ships in a provided un-labelled test-set.  This is my solution diary.


## Data Exploration
Getting the data:
```bash
$ mkdir Airbus
$ cd Airbus
$ kaggle competitions download -c airbus-ship-detection
$ unzip ./train_v2.zip -d ./Airbus/data/train_v2/
$ unzip ./test_v2.zip -d ./Airbus/data/test_v2/
$ unzip ./train_ship_segmentations_v2.csv.zip -d ./Airbus/data/
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
How many training images have/don't have ships?
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
The result is mostly no ships: 150,000 without and 81,723 ships. 

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
![alt text](./figures/train_image_masks.png)

Some ships are large and distinguishable like in the first column but others are really small and harder to detect, like the last column.  Some ships are _very_ close together, making them hard to distinguish, even when zoomed in:

![alt text](./figures/train_image_masks_closeup.png)

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

![alt text](./figures/ship_count_distribution.png)

Nearly all images have less than three ships, with most having only one.

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
![alt text](./figures/ship_areas.png)

The smallest is tiny--2 pixels in area, the largest is 25,904 pixels (4% of the image), but most are in the hundred to few-hundreds:

![alt text](./figures/ship_areas_zoom.png)


## Modeling
First we'd like to classify images according to if they have ships or not.  This way the localization model can train on a more relevant dataset of ship images and we can quickly generate empty masks for the predicted no-ship images.

Before implementing the binary classifier we're going to cut images into square quarters.  The reason for doing this is because the localization model we'll use is a Unet, and Unets tend to be trained on images for which the pixel-wise labels are approximately balanced per image.  In our case pixels of no-ship significantly out-number pixels of ship.  By cutting images in half the out-numbering will be lessened, and, on a practical dimension, normal batch sizes (16-32 images) will be able to fit into my GPU memory.

One concern about cutting images, however, is that ships will also get cut, leaving behind a slice that might be hard for Unet to recognize.  Let's see how many ships get cut:

```python
# quartify.py
from tqdm import tqdm

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

The result is `10045`, so about 12% of ships get cut.  That's more than we'd like, but the trade-off might be ok, so we'll go through with the cutting anyways and check later to see if cut-ships are indeed harder to detect.

Let's quartify images:

```python
from multiprocessing import Pool
from skimage.io import imread, imsave

imgs_root = sys.argv[0]
out_root = sys.argv[1]
paths = glob(imgs_root+'**/*.jpg', recursive=True)

df = read_csv('./data/train_ship_segmentations_v2.csv')

# Loop images
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
$ python -W ignore quartify.py ./data/train_v2/ ./data/quartered/train_v2/    # supress annoying skimage warnings
$ python -W ignore quartify.py ./data/test_v2/ ./data/quartered/test_v2/
```

The training set now has 706,997 negative instances and 63,223 positive instances.
