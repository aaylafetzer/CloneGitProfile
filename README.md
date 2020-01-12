# CloneGitProfile

A quick Python script to clone your GitLab profile to a Code folder in your Windows Documents folder

## Usage:
The script requires the ``requests`` module, which can be installed with ``pip install requests`` or by running ``pip install -r requirements.txt`` in the directory of the script.

The script can be run without arguments (``python script.py``), although you will only be able to clone one GitLab profile at a time this way.

The script can have one or several GitHub profiles passed as arguments, for example: ``python script.py apozho profile2 profile3``

If you have a larger profile, it may be beneficial to enable threading with the ``-t`` argument, for example: ``python script.py apozho -t``

## Notes
This script requires git. On Windows this can be downloaded from [git-scm.com](https://git-scm.com/download/win). You can install git on Linux distributions with:

* Debian: ``apt install git``
* Arch: ``pacman -Sy git``
* Fedora: ``yum install git-core``
