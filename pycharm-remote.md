---
layout: default
---

# Connecting PyCharm to a Remote Server

These steps and screenshots are from PyCharm Professional Edition 2017.2.3, but they should be the same or close for newer versions.

### Configuring the interpreter

PyCharm > Preferences > Project: _project name_ > Project Interpeter > _Select from dropdown or add new_ > Apply > OK

Selecting an existing interpreter:

![alt text](pycharm-remote/1.png)

Adding a new interpreter:

![alt text](pycharm-remote/2.png)

### Configuring the deployment folder (the mapping between local and remote directories)

Tools > Deployment > Configuration > Connection > _Configure connection_ > Mappings > _Configure mappings_ > OK

Configuring the connection:

![alt text](pycharm-remote/3.png)

Configuring the mapping:

![alt text](pycharm-remote/4.png)

### Set auto upload to server when a file change is made

Tools > Deployment > Upload to _server name_

Tools > Deployment > Automatic Upload

### Setting remote environment variables

Sometimes an environment variable isn't found to be defined on the remote system, even when something like ```os.environ['CUDA_VISIBLE_DEVICES']='1'``` is in the running script.  The solution is to set the environment variable directly in PyCharm:

Run > Edit Configurations > _set environment variables_ > Apply > OK

An example use case is setting `LD_LIBRARY_PATH` for using CUDA.
