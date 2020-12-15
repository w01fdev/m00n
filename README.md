# m00n
### terminal-based forensic utility

The following has been implemented so far:
* It searches the selected  path recursively for all or specific files and saves them in a csv file
* archiving as <tar.gz>

the main test is the use via a terminal. but m00n should also be usable 
as a module without any problems.

## syntax
```text
usage: m00n [-h] [-a] [-r] [-v] root file

positional arguments:
  root           root directory of the scan
  file           file into which the scan is to be written

optional arguments:
  -h, --help     show this help message and exit
  -a, --archive  archive the <.csv> file as <.tar.gz> and then delete it.
  -r, --raw      output in raw format -> partly difficult to read for humans -> default: <False>
  -v, --version  show program's version number and exit

```

## examples of usage

#### save in the program directory:
* `python m00n.py '/home/user/Pictures/' 'data.csv'`

#### save with an absolute path in raw mode as archive:
* `python m00n.py -r -a '/home/user/Pictures/' '/home/user/m00n/data.csv'`

#### further information:
* see docstrings in m00n.py

## The following implementations are planned:
* selection of what to search (file extensions ...)
* text output of statistics
* graphical output of statistics as images
* deleting files with specific file extension
* deleting files with specific file names
* deleting files with specific file size
* move or copy specific files to a directory
* information about the machine (operating system, user ...)

## Perhaps to implement:
* Standalone executeable (PyInstaller?)
