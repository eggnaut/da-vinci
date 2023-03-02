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
        font (pg.font.Font | None, optional): if you want to use a custom font. defaults to Arial font.
        italic (bool | None, optional): if using custom font, then italic. defaults to False.
        bold (bool | None, optional): if using custom font, then bold. defaults to False.
    '''
    
    if font:
        mainFont = font
    else:
        mainFont = pg.font.SysFont('Arial', 30, bold, italic)

    try:
        info = str(info)
        debugInfo = mainFont.render(info, True, '#FFFFFF', '#000000')
    except:
        print(f'davinci.debug.debug() was unable to debug the info given.\nError: {info} does not exist.\nPlease make sure the info provided is correct.\n')
        sys.exit(1)

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