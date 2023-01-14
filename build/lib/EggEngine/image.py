'''
Part of EggEngine.

Usage: 'from EggEngine import image' or 'import EggEngine.image'

Includes functions for changing images' appearances and size.

Made by @eggnaut
'''

import PIL
import pygame as pg
pg.init()

def filter(path: str) -> None:
    '''
    Will convert an image to black and white; overrides the original image.

    Args:
        path (str): path to the image you want to change
    '''
    
    image = PIL.Image.open(path)
    image = image.convert('L')
    image.save(path)

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