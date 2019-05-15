---
layout: default
---

# Cheatsheet

### Python

- Remove output from a jupyter notebook:
```bash
jupyter nbconvert notebook.ipynb --to notebook --ClearOutputPreprocessor.enabled=True --stdout > notebook_clear.ipynb
```
- Determinism with keras:

```bash
$ export PYTHONHASHSEED=10
```

```python
import numpy as np
np.random.seed(10)
import tensorflow as tf
tf.set_random_seed(10)
from keras import backend as K

session_conf = tf.ConfigProto(intra_op_parallelism_threads=1,
                              inter_op_parallelism_threads=1)
sess = tf.Session(graph=tf.get_default_graph(), conf=session_conf)
K.set_session(sess)
```

```bash
# reset pythonhashseed to normal behavior
$ export PYTHONHASHSEED=random
```

- Use matplotlib on a server: `plt.switch_backend('agg')` in the import block.
- Tensorflow/keras control gpu usage:

```python
from keras.backend.tensorflow_backend import set_session
config = tf.ConfigProto()
config.gpu_options.allow_growth=True
sess = tf.Session(config=config)
set_session(sess)
```

```python
from keras.backend.tensorflow_backend import set_session
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.5
set_session(tf.Session(config=config))
```

- Use tqdm with multiprocessing:

```python
pool = multiprocessing.Pool(n_processes=4)
for _ in tqdm(pool.imap(map_function, input_iterable), total=len(input_iterable)):
    pass
```

- Make a movie with opencv.  A list of video codecs is [here](https://gist.github.com/takuma7/44f9ecb028ff00e2132e).

```python
from cv2 import VideoWriter, VideoWriter_fourcc

video_dest = 'video.mp4'
fps = 1
im_rows, im_cols = 100, 100
codec = VideoWriter_fourcc(*'mp4v')
video = VideoWriter(video_dest, codec, fps, (im_cols,im_rows))

for frame in range(nframes):
    im = np.random.random((im_rows, im_cols, 3))*255
    im = im.astype(np.uint8)
    video.write(im)

video.release()
```


### Bash

- Suppress tensorflow warnings: `export TF_CPP_MIN_LOG_LEVEL=2`.
- Check if images in a folder are corrupt: `$ find folder/ -name "*.jpg" | xargs jpeginfo -c | grep "WARNING"`.
- Pretty print json: `$ python -m json.tool file.json`.
- Pretty print h5: `$ h5dump file.h5`.  Use `-H` to only show headers.
- Force python's output buffer to flush: `-u`, e.g.,  `$ nohup python -u script.py &`.
- Make video using images in a folder: `$ ffmpeg -r $FPS -pattern_type glob -i '*.jpg' movie.mp4`.
- sed example: `$ sed -i .bak "s/<find_regex>/<replace_regex>/g" file.txt`.
- awk example: `$ awk -F, {print $1} file.csv`.
- xargs example: `cat file_names.txt | xargs -I % scp remote:% dest/`.



### Misc

- Weight initializations best used for various activation functions:

| Activation |  Initializer  |               Scaling               |
|:----------:|:-------------:|:-----------------------------------:|
|   Linear   |  lecun_normal |     $$\frac{1}{\sqrt{n_{in}}}$$     |
|    ReLU    |   he_normal   |     $$\sqrt{\frac{2}{n_{in}}}$$     |
|    Tanh    | glorot_normal | $$\sqrt{\frac{2}{n_{in}+n_{out}}}$$ |
