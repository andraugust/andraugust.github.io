---
layout: default
---

# Cheatsheet

I'll probably forget these are here and look them up on stack exchange... ..sigh..

## Python

- Best way to install tensorflow such that all cuda dependencies are handled correctly:
```bash
conda create tf-env python=3.6
conda activate tf-env
conda install -c anaconda tensorflow-gpu=1.12
```

- Remove output cells from a jupyter notebook:
```bash
jupyter nbconvert notebook.ipynb --to notebook --ClearOutputPreprocessor.enabled=True --stdout > notebook_clear.ipynb
```

- Assign arguments of a class to self:
```python
class Foo():
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
#
foo = Foo(a=1,b=2)
print(foo.a)  # 1
```

- Call a function using a string:
```python
def foo(arg):
    pass
# One way
locals()['foo'](arg)
# Another way
eval('foo')(arg)
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
# Init
video_dest = 'video.mp4'
fps = 1
im_rows, im_cols = 100, 100
codec = VideoWriter_fourcc(*'mp4v')
video = VideoWriter(video_dest, codec, fps, (im_cols,im_rows))
# Main loop
for frame in range(nframes):
  im = np.random.random((im_rows, im_cols, 3))*255
  im = im.astype(np.uint8)
  video.write(im)
video.release()
```

- Print over the current line:
```python
import sys
import time
# Constants
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
# Main loop
iter = 0
for i in range(1000):
  iter += 1
  sys.stdout.write(ERASE_LINE)
  print('Dot dot dot.' + '.'*(iter%3))
  sys.stdout.write(CURSOR_UP_ONE)
  time.sleep(0.5)
```

- Logging:
```python
import logging
mode = 'dev'
log_level = logging.DEBUG if mode == 'dev' else logging.INFO
logging.basicConfig(level=log_level, format='%(message)s') # format so the line isn't prefixed with logging info
logging.debug('This prints during development')
logging.info('This prints during development and release')
```

## Bash

- Suppress tensorflow warnings: `export TF_CPP_MIN_LOG_LEVEL=2`.
- Check if images in a folder are corrupt: `$ find folder/ -name "*.jpg" | xargs jpeginfo -c | grep "WARNING"`.
- Pretty print json: `$ python -m json.tool file.json`.
- Pretty print h5: `$ h5dump file.h5`.  Use `-H` to only show headers.
- Force python's output buffer to flush: `-u`, e.g.,  `$ nohup python -u script.py &`.
- Make video using images in a folder: `$ ffmpeg -r $FPS -pattern_type glob -i '*.jpg' movie.mp4`.
- Example sed: `$ sed -i .bak "s/<find_regex>/<replace_regex>/g" file.txt`.
- Example awk: `$ awk -F, '{ print $1 }' file.csv`.
- Example xargs: `cat file_names.txt | xargs -I % scp remote:% dest/`.
- Modify shell behavior:  `set -ue` at the top of a script to make an error message occur when an unassigned variable is referenced and exit if a subprocess returns non-zero exit status.
- Parallel processing:
```bash
cmd1 &
cmd2 &
wait
cmd3
```

- Display json in terminal: `jq --color-output . file.json | more -R`

## Other

- How to make a continuous approximation to a step function starting at $$0$$ and ending at $$a$$, using logistic functions: $$\frac{1}{1+\exp(-kx)} - \frac{1}{1+\exp(-k(x-a))}$$.