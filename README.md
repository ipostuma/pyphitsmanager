# pyphitsmanager

This python library aims to help developing and managing a PHITS simulation. When
installed you'll be able to execute the python script ```PHITSmanager -h```. The -h
parameter will *help* and guide you through the usage of the script.

### version 0.1.1
it is still a development version, but these commands work:

+ ```PHITSmanager init PATH``` -> start a new PHITSmanager project
+ ```PHITSmanager cd PATH``` -> copy an PHITSmanager project into an existing one
+ ```PHITSmanager build``` -> build the PHITS input file

Requirements
------------

+ Python. Versions >= 3 are not supported

Installation
------------

Installing the latest stable repo is an easy task, just:

```
pip install git+https://github.com/ipostuma/pyphitsmanager.git
```

While if you want to get the latest *development* **unstable** repo, just execute
the command above and add this trailing string ```@dev``` .

###### to uninstall:

```
pip uninstall pyphitsmanager
```

Contacts
--------
e-mail: ian.postuma [аt] gmail.com

List of authors: Ian Postuma

License
-------
[GNU GPL v3](https://github.com/ipostuma/pyphitsmanager/blob/master/LICENSE)
