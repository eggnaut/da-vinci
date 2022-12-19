'''
Part of EggEngine.

Usage: 'from egg import files' or 'import egg.files'

Includes functions for reading content from and writing content to files.

Made by eggnaut
'''

import sys

def readFile(file: str) -> str | int | bytes:
    '''
    Reads the contents of a file.

    Args:
        file (str): the path to the file

    Returns:
        str | int | bytes: the contents of the file
    '''
    
    try:
        with open(file, 'r') as originalFile:
            content = originalFile.read()
        return content

    except FileNotFoundError:
        print(f'\nengine.files.readFile() was unable to read the file given.\nFileNotFoundError: {file} does not exist.\nPlease make sure the path provided is correct.\n')
        sys.exit()

def writeFile(file: str, content: str | int | bytes) -> None:
    '''
    Writes/saves content to a file.

    Args:
        file (str): the path to the file
        content (str | int | bytes): the content you want in the file
    '''
    
    with open(file, 'w') as originalFile:
        originalFile.write(content)