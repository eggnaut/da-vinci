'''
Part of EggEngine.

Usage: 'from EggEngine import image' or 'import EggEngine.image'

Includes functions for changing images' appearances and size.

Made by @eggnaut
'''

import PIL
import io
import urllib.request as ul
import pygame as pg
pg.init()

def loadUrl(url: str) -> bytes:
    '''
    Loads an image and returns it as bytes, which can be used with Pygame.
    
    Args:
        url (str): the url to the image
        
    Returns:
        img (bytes): the image, in bytes form, can be used with pygame.image.load()
    '''
    
    imgUrl = ul.urlopen(url).read()
    img = io.BytesIO(imgUrl)
    
    return img

def filter(path: str, type: str, show: bool = False) -> None:
    '''
    Applies a filter to the given image; overrides the original image

    Args:
        path (str): _description_
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
