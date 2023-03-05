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


Usage: 'from davinci import fps' or 'import davinci.fps'

Includes a function to display the frames per second of a Pygame window.

Made by @eggnaut
'''

import pygame as pg
pg.init()

def fpsDisplay(wn: pg.Surface, 
               clockObj: pg.time.Clock, 
               fontSize: int | None = 20, 
               bold: bool | None = False, 
               italic: bool | None = False, 
               pos: tuple | None = (15, 15), 
               color: str | tuple = '#FFFFFF', 
               bgColor: str | tuple = '#000000'
               ):
    '''
    Displays the frames per second of the current Pygame window. Useful for determining a game's performance.

    Args:
        wn (pg.Surface): The Pygame window.
        clockObj (pg.time.Clock): A Pygame clock object, used to update the window.
        fontSize (int | None, optional): Size of the font (Arial). Defaults to 20.
        bold (bool | None, optional): If the text should be bolded. Defaults to False.
        italic (bool | None, optional): If the text should be italicized. Defaults to False.
        pos (tuple | None, optional): The position of the text as a tuple, (x, y). Defaults to (15, 15).
        color (str | tuple, optional): The color of the text. Defaults to '#FFFFFF'.
        bgColor (str | tuple, optional): The background color of the text. Defaults to '#000000'.
    '''
    
    font = pg.font.SysFont('Arial', fontSize, bold, italic)
    fps = round(clockObj.get_fps(), 2)
    text = font.render(str(fps), True, color, bgColor)
    wn.blit(text, pos)
