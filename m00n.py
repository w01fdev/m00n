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


class DirectoryScanner:
    """Forensic search for directories and files on the hard drive."""

    def __init__(self, root):
        """Initalisation of the class.

        :param root: <str>
            the root directory from which the scan should start.
        """

        self._root = root
        self._data = []

        # counter
        self._dirs_ix = 0
        self._files_ix = 0

    def get_data(self):
        """Returns the collected data.

        :return: <list>
        """

        return self._data

    def get_directory_counter(self):
        """Returns the directory counter.

        :return: <int>
        """

        return self._dirs_ix

    def get_files_counter(self):
        """Returns the files counter.

        :return: <int>
        """

        return self._files_ix

    def get_total_counter(self):
        """Returns the complete counter (directories + files)

        :return: <int>
        """

        return self._dirs_ix + self._files_ix

    def get_all_counters(self):
        """Returns all counters in a list (total, directories, files).

        :return: <list>
        """

        return self.get_total_counter(), self.get_directory_counter(), self.get_files_counter()

    def run(self):
        """Starts a forensic scan and returns the data as <dict> in a <list>.

        :return: <list>
        """

        for self._dir_ix, (root, dirs, files) in enumerate(os.walk(self._root)):
            self._dirs_ix += 1
            self._data.append({'path': root})
            print(root)

            for filename in files:
                self._files_ix += 1
                path = os.path.join(root, filename)
                self._data.append({'path': path})
                print(path)
        else:
            self._print_scan_results()
            return self._data

    def _print_scan_results(self):
        """Outputs a small text-based statistic of the result."""

        print('\nscan executed: total: {:,} | directories: {:,} | files: {:,}'.format(*self.get_all_counters()))


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


def _console():
    """Arguments for control via the console.

    :return: <class 'argparse.Namespace'>
    """

    parser = argparse.ArgumentParser(prog='m00n')
    parser.add_argument('root', action='store', help='root directory of the scan')
    parser.add_argument('file', action='store', help='file into which the scan is to be written')
    parser.add_argument('-v', '--version', action='version', version='version: {} ({})'.format(
        program_version, program_date
    ))

    return parser.parse_args()


def main():
    """Main function of the program."""

    args = _console()

    if args.root and args.file:
        scan = DirectoryScanner(args.root)
        data = scan.run()
        csv_writer(args.file, data)


if __name__ == '__main__':
    main()
