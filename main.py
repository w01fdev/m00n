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

import os


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
        data.append(root)

        for filename in files:
            files_ix += 1
            total_ix += 1
            path = os.path.join(root, filename)
            print(path)
            data.append(path)
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


def main():
    """Main function of the program."""

    data, summary = directory_scanner('/home/anonymous/Pictures/W01f/pass/')


if __name__ == '__main__':
    main()
