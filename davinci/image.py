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

Usage: 'from davinci import image' or 'import davinci.image'

Includes functions for changing images' appearances and size.

Made by @eggnaut
'''

import PIL
import pygame as pg
pg.init()

def filter(path: str, type: str, show: bool = False) -> None:
    '''
    Applies a filter to the given image; overrides the original image

    Args:
        path (str): the path to the file
        type (str): type of filter you want; options are: grayscale, blur, contour, emboss
        show (bool): if you want to see the filtered image. defaults to False.
    '''
    image = PIL.Image.open(path)
    
    if type == 'grayscale':
        image = image.convert('L')
        image.save(path)
    elif type == 'contour':
        image = image.filter(PIL.ImageFilter.CONTOUR)
        image.save(path)
    elif type == 'blur':
        image = image.filter(PIL.ImageFilter.BLUR)
        image.save(path)
    elif type == 'emboss':
        image = image.filter(PIL.ImageFilter.EMBOSS)
        image.save(path)
        
    if show: image.show()

def brighten(image: pg.Surface, brightness: tuple | None = (255, 255, 255)) -> pg.Surface:
    '''
    Brightens an image using Pygame's BLEND_RGB_ADD special flag. Intensity can be customized.

    Args:
        image (pg.Surface): the original image
        brightness (tuple | None, optional): an RGB value meant to change the brightness. defaults to (255, 255, 255).

    Returns:
        newImage (pg.Surface): the original image, but brighter, the intensity depends on the brightness arg
    '''
    
    newImage = image.fill(brightness, special_flags = pg.BLEND_RGB_ADD)

    return newImage

def darken(image: pg.Surface, darkness: tuple | None = (0, 0, 0)) -> pg.Surface:
    '''
    Darkens an image using Pygame's BLEND_RGB_SUB special flag. Intensity can be customized.

    Args:
        image (pg.Surface): the original image
        brightness (tuple | None, optional): an RGB value meant to change the brightness. defaults to (0, 0, 0).

    Returns:
        newImage (pg.Surface): the original image, but darker, the intensity depends on the darkness arg
    '''
    
    newImage = image.fill(darkness, special_flags = pg.BLEND_RGB_SUB)

    return newImage

def scaleImage(image: pg.Surface, scale: int | None = 2) -> pg.Surface:
    '''
    Scales an image in a much way that makes the code more cleaner, without the long lines.

    Args:
        image (pg.Surface): the original image
        scale (int | None, optional): the scale factor that will be applied. defaults to 2.

    Returns:
        newImage (pg.Surface): the original image, but scaled up or down
    '''
    
    newImage = pg.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))

    return newImage
