#    An all-purpose framework/library written with and for Python.
#    Copyright (C) 2023  Dishant B. (eggnaut)
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#    USA

'''
Part of da vinci.

Usage: 'from davinci import files' or 'import davinci.files'

Includes functions for reading content from files, writing content to files, and more!

Made by @eggnaut
'''

import sys
import os

def totalLines(path: str) -> int:
    '''
    Returns the total number of lines (the sum of all the files' lines) in a directory.

    Args:
        path (str): the path to the directory

    Returns:
        total (int): the total number of lines
    '''
    
    total = 0
    allFiles = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    for file in allFiles:
        with open(file, 'r') as f:
            lines = f.readlines()
            total += len(lines)

    return total

def numLines(path: str) -> int:
    '''
    Returns the number of lines in the file.

    Args:
        path (str): the path to the file

    Returns:
        length (int): the number of lines in the file
    '''

    with open(path, 'r') as file:
        lines = file.readlines()

    return len(lines)

def readFile(path: str) -> any:
    '''
    Reads the contents of a file.

    Args:
        path (str): the path to the file

    Returns:
        contents (any): the contents of the file
    '''
    
    try:
        with open(path, 'r') as originalFile:
            content = originalFile.read()
        return content

    except FileNotFoundError:
        print(f'\ndavinci.files.readFile() was unable to read the file given.\nFileNotFoundError: {path} does not exist.\nPlease make sure the path provided is correct.\n')
        sys.exit(1)

def writeFile(path: str, content: any, create: bool = False) -> None:
    '''
    Writes/saves content to a file.

    Args:
        path (str): the path to the file
        content (any): the content you want in the file
        create (bool): if the file doesn't exist, should it be created. defaults to False.
    '''
    
    try:
        with open(path, 'w') as originalFile:
            originalFile.write(content)
    except FileNotFoundError:
        if create:
            with open(path, 'x') as originalFile:
                originalFile.write(content)
        else:
            print(f'\ndavinci.files.writeFile() was unable to read the file given.\nFileNotFoundError: {path} does not exist.\nPlease make sure the path provided is correct.\n')
            sys.exit(1)