#!/usr/bin/env python

"""m00n
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
import time

from modules.program import program_version, program_date


class DirectoryScanner:
    """Forensic search for directories and files on the hard drive."""

    def __init__(self, root, mode='human'):
        """Initalisation of the class.

        :param root: <str>
            the root directory from which the scan should start.
        :param mode: <bool> -> std: <human>
            If the argument is set to <stats> | <human>, besides the
            path, further information about the directory or file is
            collected. this includes time of creation and modification,
            user and group ... further information in the python
            documentation under <os.stat>.

            there are different modes:
            1. <paths>
                here only the path is saved without any additional
                information. this is by far the fastest method.
            2. <stats>
                file statistics are requested. these are given in raw
                form. this means that some of them are not or only with
                difficulty readable by humans.
            3. <human>
                as far as possible, the data is converted into a
                human-friendly format so that it can be read without
                the need for further tools. at the same time, however,
                care is taken to ensure that it can still be easily
                imported and used in tools such as pandas in order to
                waste as little code and time as possible in data
                preparation.

            caution: if the argument is set to <stats> | <human>, much
            more time is needed, because more information is determined
            and in the <human> mode it has to be processed.
        """

        self._root = root
        self._mode = mode
        self._data = []
        self._keys = []
        self._set_csv_fieldnames()
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

    def get_csv_fieldnames(self):
        """Get a list with the keys of the collected values.

        these can be passed as field names in the <csv> module.

        :return: <list>
        """

        return self._keys

    def run(self):
        """Starts a forensic scan and returns the data as <dict> in a <list>.

        :return: <list>
        """

        for self._dir_ix, (root, dirs, files) in enumerate(os.walk(self._root)):
            self._dirs_ix += 1
            self._run_path_processing(root)
            print(root)

            for filename in files:
                self._files_ix += 1
                path = os.path.join(root, filename)
                self._run_path_processing(path)
                print(path)
        else:
            self._print_scan_results()
            return self._data

    def _print_scan_results(self):
        """Outputs a small text-based statistic of the result."""

        print('\nscan executed: total: {:,} | directories: {:,} | files: {:,}'.format(*self.get_all_counters()))

    def _run_path_processing(self, path):
        """Processes the path according to the user input.

        is called from method <run>

        :param path: absolute path to a directory or file
        """

        if type(self._mode) == str:
            if self._mode == 'paths':
                self._data.append({'path': path})
            elif self._mode == 'stats' or self._mode == 'human':
                data = {}
                stat = os.stat(path)
                values = [stat.st_uid, stat.st_gid, stat.st_mode,
                          stat.st_dev]

                if self._mode == 'stats':
                    values.extend([stat.st_ctime, stat.st_atime, stat.st_mtime, stat.st_size])

                if self._mode == 'human':
                    values.extend(
                        [
                            # importable with module <datetime.datetime.fromisoformat()>
                            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat.st_ctime)),
                            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat.st_atime)),
                            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat.st_mtime)),
                            # size in megabyte
                            '{:08.2f}'.format(round(stat.st_size / (1024 * 1024), 2)),
                        ]
                    )

                values.append(path)

                for key, value in zip(self._keys, values):
                    data[key] = value
                else:
                    self._data.append(data)

            else:
                raise ValueError('only the following is accepted as input: <paths> | <stats> | <human>')
        else:
            raise TypeError('argument must be a <str>')

    def _set_csv_fieldnames(self):
        """Currently only mode <paths> implemented. for this reason private."""

        if self._mode == 'paths':
            self._keys = ['path', ]
        elif self._mode == 'stats' or self._mode == 'human':
            self._keys = ['user_id', 'group_id', 'file_mode',
                          'device_identifier', 'created', 'last_access',
                          'last_modified', 'file_size', 'path']


def csv_writer(file, data, fieldnames):
    """Write the data in a file.

    :param file: <str>
        filename in which the data is to be saved as <.csv>.
        examples:
            <'data.csv'>
            <'/home/user/m00n/data.csv'>
    :param data: <list>
        a list of <dicts> with data from the <directory_scanner>.
    :param fieldnames: <list>
        a list containing field names.
    """

    with open(file, 'w', newline='') as csv_file:
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
    parser.add_argument('-m', '--mode', action='store', default='human',
                        help='3 modes are available: <paths> | <stats> | <human> -> default: <human>')
    parser.add_argument('-v', '--version', action='version', version='version: {} ({})'.format(
        program_version, program_date
    ))

    return parser.parse_args()


def main():
    """Main function of the program."""

    args = _console()

    if args.root and args.file:
        scan = DirectoryScanner(args.root, mode=args.mode)
        data = scan.run()
        fieldnames = scan.get_csv_fieldnames()
        csv_writer(args.file, data, fieldnames)


if __name__ == '__main__':
    main()
