# m00n

m00n is a terminal-based forensic utility. It searches the selected 
path recursively for all or specific files and saves them in a csv file.

the main test is the use via a terminal. but m00n should also be usable 
as a module without any problems.

## syntax

python moon [optional args] **root** **file**



## examples of use

#### save in the program directory with paths only mode:
python m00n.py -m 'paths' '/home/user/Pictures/' 'data.csv'

#### save with an absolute path:
python m00n.py '/home/user/Pictures/' '/home/user/m00n/data.csv'

#### further information:
python m00n.py -h

see docstrings in m00n.py

## The following implementations are planned:
* selection of what to search (file extensions ...)
* text output of statistics
* graphical output of statistics as images
* deleting files with specific file extension
* deleting files with specific file names
* deleting files with specific file size
* move or copy specific files to a directory
* pack files as archive
* information about the machine (operating system, user ...)

## Perhaps to implement:
* Standalone executeable (PyInstaller?)
