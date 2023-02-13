'''
Part of da vinci.

Usage: 'from davinci import files' or 'import davinci.files'

Includes functions for reading content from and writing content to files.

Made by @eggnaut
'''

import sys

def readFile(path: str) -> str | int | bytes:
    '''
    Reads the contents of a file.

    Args:
        path (str): the path to the file

    Returns:
        str | int | bytes: the contents of the file
    '''
    
    try:
        with open(path, 'r') as originalFile:
            content = originalFile.read()
        return content

    except FileNotFoundError:
        print(f'\ndavinci.files.readFile() was unable to read the file given.\nFileNotFoundError: {path} does not exist.\nPlease make sure the path provided is correct.\n')
        sys.exit()

def writeFile(path: str, content: str | int | bytes, create: bool = False) -> None:
    '''
    Writes/saves content to a file.

    Args:
        path (str): the path to the file
        content (str | int | bytes): the content you want in the file
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
            sys.exit()