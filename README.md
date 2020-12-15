# w01fm00n
### terminal-based forensic utility

The following has been implemented so far:
* It searches the selected path recursively for all or specific files and saves them in a csv file
* archiving as <tar.gz>

the main test is the use via a terminal. but m00n should also be usable 
as a module without any problems.

## syntax
```text
usage: w01fm00n [-h] [-a] [-r] [-v] root file

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
* `python w01fm00n.py '/home/user/Pictures/' 'data.csv'`

#### save with an absolute path in raw mode as archive:
* `python w01fm00n.py -r -a '/home/user/Pictures/' '/home/user/m00n/data.csv'`

#### further information:
* see docstrings in w01fm00n.py

## planned future implementations and improvements:
https://github.com/w01fdev/w01fm00n/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement
