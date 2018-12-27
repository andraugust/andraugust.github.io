---
layout: page
title: "Snippets and Tidbits"
permalink: /snippets/
---

<h2><center>Snippets and Tidbits</center></h2>

This is an ever growing list of code snippets and tidbits I've found useful.  Putting them here prevents them from getting lost or forgotten and gives others an opportunity to use them 👍.

<center><img src="banner2.jpg"></center>
<center><p><em>Don't forget your curlyboys!</em></p></center>

<hr>
<br />
## Python
__Label encoding__ Convert data-labels back and forth between categorical and one-hot. (One-hot is a probability distribution.) Note that in addition to LabelBinarizer sklearn has a OneHotEncoder object, but unfortunately it doesn't support inverse_transform(), so LabelBinarizer might be preferred.  Also, sometimes it's more convenient to skip sklearn.LabelBinarizer all-together and "roll your own" encoder by making a dictionary and pickling it.  This way the encoding will be more accessible across scripts.
```python
from sklearn.preprocessing import LabelBinarizer

lb = LabelBinarizer()
# encode labels
Y_cat = import_some_categorical_labels()
Y_onehot = lb.fit_transform(Y_cat)  # fit_transform automatically detects the number of categories
# encode new labels using same encoding
Y_new_cat = import_some_new_categorical_labels()
Y_new_onehot = lb.transform(Y_new_cat)
# decode labels
Y_predict = make_a_prediction(Y_onehot)
Y_predict_cat = lb.inverse_transform(Y_predict)
```

__Keras training callbacks__ Train a model in keras while doing three things: maintain a running csv-log of training and validation error, save the model if its validation error is smallest, stop training if validation error didn't decrease after a threshold number of epochs.
```python
from keras.callbacks import CSVLogger, ModelCheckpoint, EarlyStopping

logger = CSVLogger('/log/path/file.csv')
saver = ModelCheckpoint('/model/path/file.h5', monitor='val_loss', verbose=True, save_best_only=True, mode='min')
stopper = EarlyStopping(monitor='val_loss', patience=patience, verbose=True, mode='auto')

model.fit(X,Y,...,callbacks=[logger,saver,stopper])
```

__DIY batch training in Keras__.  Sometimes the data needed to train a model doesn't fit entirely into memory, so it's necessary to load data in chunks.  Keras has some functionality for chunk loading, but DIY isn't hard and you gain some control.  The major thing to notice in this snippet is that validation error isn't evaluated until the end of a chunk, which can speed up training significantly.
```python
chunk_sz = 1000   # number of samples to load at a time
N = 1000000       # total number of samples
n_epochs = 10     # number of times to loop through the whole dataset
n_batches = int(np.ceil(float(N)/float(chunk_sz)))
for e in range(n_epochs):
    for b in range(n_batches):
        print('Epoch: %s/%s    Batch: %s/%s' % (e+1,n_epochs,b+1,n_batches))
        X_tr, Y_tr = get_batch(b)
        val_data = (X_te, Y_te) if b==n_batches-1 else None
        model.fit(X_tr, Y_tr,
                  batch_size=128,
                  nb_epoch=1,
                  validation_data=val_data,
                  verbose=b==n_batches-1)
```

__Directory walking__. Extremely useful for getting all filenames in a root directory, regardless of if they're leaves or not.
```python
import os
for root, subdirs, files in os.walk('/some/base/path/'):
    for file in files:
        print(os.path.join(root,file))
```

__Multiprocessing__ Run multiple processes in parallel and use a shared-memory variable to keep track of progress.  Note that more processors doesn't imply more speed, especially if the process is IO-bound.  See <a href="http://chriskiehl.com/article/parallelism-in-one-line/">Chris Kiehl's</a> blog for more info.
```python
from multiprocessing.dummy import Pool, Value

inputs = make_an_iterable()

i = Value('i',0) # progress counter
def fuction_to_run(input):
    i.value += 1
    if i.value % 100 == 0: print('I\'ve done %i so far.' % i.value)
    # do stuff to input here

max_proc = multiprocessing.cpu_count()
pool = Pool(max_proc-2)
pool.map(function_to_run,inputs)
pool.close()
pool.join()
```

__Command-line arguments__ A sophisticated way for python scripts to accept command-line arguments.  Allows for a man page, default initializations, and 'dash' style inputs.  Man page is accessed via `$ python program.py -h`.
```python
import argparse

def get_args():
    """Read command-line input"""
    parser = argparse.ArgumentParser(description='Description of program.')
    parser.add_argument('-v1', metavar='v1', type=int, default=15, help='description of variable v1')
    parser.add_argument('-v2', metavar='v2', type=float, default=0.5, help='description of v2')
    parser.add_argument('-v3', metavar='v3', type=str, default='myfavoritestring', help='description of v3')
    return parser.parse_args()

# extract params
args = get_args()
v1, v2, v3 = args.v1, args.v2, args.v3
```
<hr>
<br />
## Geotiff Processing
Geotiff is a popular data format used for saving satellite images.  It allows _georeference_ data to be stored with images, providing information about how images fit on a map.  Here are some functionalities that I've found useful for working with geotiffs in python.  The primary package that gets used is called _GDAL_, the geospacial data abstraction library.

* View file info:
```bash
$ gdalinfo example.tiff
```
* Basic data extraction:
```python
from osgeo import gdal
imobj = gdal.Open('/path/to/image.tiff')
# Get shape of tif
h,w,d = imobj.RasterYSize, imobj.RasterXSize, imobj.RasterCount
# Get raster bands as numpy array
arr = imobj.ReadAsArray()
# Get a single raster band as numpy array, e.g. band 1
band = imobj.GetRasterBand(1).ReadAsArray()
```
* Save an array as geotiff such that it has the same geo-reference data as a pre-existing tiff.  This is useful for making masks or heatmaps that overlay the pre-existing tiff.
```python
def array2tif(arr,inf,outf):
    """
    Copies the meta-features of the tif located at inf to a new tif located at outf, where outf has a raster band defined by arr.
    """
    driver = gdal.GetDriverByName('GTiff')
    tif_in = gdal.Open(inf)
    # create new tif
    nbands = arr.shape[2]
    tif_out = driver.Create(outf, tif_in.RasterXSize, tif_in.RasterYSize, nbands, gdal.GDT_Byte)
    tif_out.SetGeoTransform(tif_in.GetGeoTransform())
    tif_out.SetProjection(tif_in.GetProjection())
    # write bands
    for band in range(nbands):
        tif_out.GetRasterBand(band).WriteArray(arr[:,:,band])
    # close objects
    del tif_in
    del tif_out
```

More great geotiff snippets [here](https://pcjericks.github.io/py-gdalogr-cookbook/).

<hr>
<br />
## Bash
__No hang-up__ Run a python program such that you can disconnect the terminal session and it will continue to run.  Printed output goes to a file called `nohup.out`, the option `-u` ensures that output gets flushed here regularly.
```bash
$ nohup python -u script.py &
```
For multiple scripts to run in sequence:
```bash
$ nohup bash -c "python -u script1.py; python -u script2.py;" &
```

__Text file access__.  These commands are useful for accessing text files.  When the text file is big this is more convenient than using a graphical editor.
```bash
# Print a specific line, e.g. 36
$ sed -n 36p file.txt
# Print the end starting at a specific line
$ tail -n +36 file.txt
# Print lines between a range
$ sed -n '36,63p' file.txt
```
