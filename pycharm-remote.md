---
layout: default
---

# Connecting PyCharm to Remote Server

1. Configure interpreter:

PyCharm > Preferences > Project: _project name_ > Project Interpeter > _Select from dropdown or add new_ > Apply > OK

Selecting an existing interpreter:

![alt text](pycharm-remote/1.png)

Adding a new interpreter:

![alt text](pycharm-remote/2.png)

2. Configure deployment folder:

Tools > Deployment > Configuration > Connection > _Configure connection_ > Mappings > _Configure mappings_ > OK

Configured connection:

![alt text](pycharm-remote/3.png)

Configured path mapping:

![alt text](pycharm-remote/4.png)

3. Set up auto upload to server:

Tools > Deployment > Upload to _server name_
Tools > Deployment > Automatic Upload
