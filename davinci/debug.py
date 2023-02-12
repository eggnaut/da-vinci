'''
Part of da vinci.

Usage: 'from davinci import debug' or 'import davinci.debug'

Includes functions for debugging in Python as well as OS-related functions.

Made by @eggnaut
'''

import sys
import platform as pm
import pygame as pg
pg.init()

def debug(info, wn: pg.Surface, pos: tuple | None = (0, 0), font: pg.font.Font | None = None, italic: bool | None = False, bold: bool | None = False) -> None:
    '''
    Given a variable, this function will display it's value on a Pygame window.

    Args:
        info (any): a variable, will be the info displayed for debugging ease
        wn (pg.Surface): the Pygame window that info will be displayed on
        pos (tuple | None, optional): position in coordinates on window. defaults to (0, 0).
        font (pg.font.Font | None, optional): if you want to use a custom font. defaults to None.
        italic (bool | None, optional): if using custom font, then italic. defaults to False.
        bold (bool | None, optional): if using custom font, then bold. defaults to False.
    '''
    
    if font:
        mainFont = font
    else:
        mainFont = pg.font.SysFont('Arial', 30, bold, italic)

    try:
        debugInfo = mainFont.render(info, True, '#FFFFFF', '#000000')
    except:
        print(f'\nEggEngine.debug.debug() was unable to debug the info given.\nError: {info} does not exist.\nPlease make sure the info provided is correct.\n')
        sys.exit()

    wn.blit(debugInfo, pos)

def checkOS(precise: bool = False) -> str:
    '''
    Tells what operating system the code is being run on, allows for more precise results.

    Args:
        precise (bool, optional): whether you want precise (granular) checking or lenient checking. defaults to False.

    Returns:
        oper (str): the name of the operating system
    '''
    
    if precise:
        if sys.platform() == 'aix':
            oper = 'AIX'
        elif sys.platform() == 'emscripten':
            oper = 'Emscripten'
        elif sys.platform() == 'linux':
            oper = 'Linux'
        elif sys.platform() == 'wasi':
            oper = 'WASI'
        elif sys.platform() == 'win32' or sys.platform() == 'cygwin':
            oper = 'Windows'
        elif sys.platform() == 'darwin':
            oper = 'macOS'
    else:
        oper = pm.system()
        
    return oper