---
layout: default
---

# Cheatsheet

- Use matplotlib on a server: `plt.switch_backend('agg')` in the import block.

- Pretty print json at command line: `$ python -m json.tool file.json`.

- Inspect h5 at command line: `$ h5dump file.h5`.  Use `-H` to only show headers.

- Bash kill script if subprocess returns non 0 exit code: `-e`.  Useful for bash scripts that run python scripts.  Useful for `$ nohup bash -e script.sh &`.

- Python force output buffer to flush: `-u`.  Useful for `$ nohup python -u script.py &`.

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

- Use `tqdm` with `multiprocessing`:
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

- Make a video out of images in a folder: `$ ffmpeg -r $FPS -pattern_type glob -i '*.jpg' movie.mp4`.

- sed find and replace text: `$ sed -i .bak 's/<find_regex>/<replace_regex>/g' file.txt`.
