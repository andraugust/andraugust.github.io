---
layout: default
---

# Connecting PyCharm to a Remote Server

These steps were tested on PyCharm Professional Edition 2017.2.3.

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
