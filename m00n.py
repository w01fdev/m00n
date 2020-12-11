#!/usr/bin/env python3

"""w01f m00n
Copyright (C) 2020 w01f - https://github.com/w01fdev/

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

########################################################################

w01f hacks from Linux for Linux!

fck capitalism, fck patriarchy, fck racism, fck animal oppression ...

########################################################################
"""


import argparse
import csv
import os

from modules.program import program_version, program_date


def csv_writer(file, data):
    """Write the data in a file.

    :param file: <str>
        filename in which the data is to be saved as <.csv>.
        examples:
            <'data.csv'>
            <'/home/user/m00n/data.csv'>
    :param data: <list>
        a list of <dicts> with data from the <directory_scanner>.
    """

    with open(file, 'w', newline='') as csv_file:
        fieldnames = ['path', ]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def directory_scanner(root):
    """Scans the directory with all subdirectories.

    :param root: <str>
        the root directory from which the scan should start.
    :return: <list>, <dict>
        returns in first position a list containing the directories and
        files. In second position a <dict> with 3 keys (directories,
        files, total)
    """

    data = []
    dirs_ix = 0
    files_ix = 0
    total_ix = 0

    for dir_ix, (root, dirs, files) in enumerate(os.walk(root), start=0):
        dirs_ix += 1
        total_ix += 1
        print(root)
        data.append({'path': root})

        for filename in files:
            files_ix += 1
            total_ix += 1
            path = os.path.join(root, filename)
            print(path)
            data.append({'path': path})
    else:
        summary = {
            'directories': dirs_ix,
            'files': files_ix,
            'total': total_ix,
        }
        print('\nscan executed: total: {:,} | directories: {:,} | files: {:,}'.format(
            summary.get('total'), summary.get('directories'), summary.get('files'))
        )

    return data, summary


def _console():
    """Arguments for control via the console.

    :return: <class 'argparse.Namespace'>
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--root', action='store', help='root directory of the scan')
    parser.add_argument('-f', '--file', action='store', help='file into which the scan is to be written')
    parser.add_argument('-v', '--version', action='version', version='version: {} ({})'.format(
        program_version, program_date
    ))

    return parser.parse_args()


def main():
    """Main function of the program."""

    args = _console()

    if args.root and args.file:
        data, summary = directory_scanner(args.root)
        csv_writer(args.file, data)


if __name__ == '__main__':
    main()
