---
layout: default
---

# Cheatsheet

- Use matplotlib on a server: `plt.switch_backend('agg')` in the import block.

- Pretty print json at command line `$ python -m json.tool file.json`

- Inspect h5 at command line: `$ h5dump file.h5`.  Use `-H` to only show headers.

- Bash kill script if subprocess returns non 0 exit code: `-e`.  Useful for bash scripts that run python scripts.  Useful for `$ nohup bash -e script.sh &`.

- Python force output buffer to flush: `-u`.  Useful for `$ nohup python -u script.py &`.
