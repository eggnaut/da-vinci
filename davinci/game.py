'''
Part of da vinci.

Usage: 'from davinci import game' or 'import davinci.game'

Useful functions and classes for game development with Pygame.

Made by @eggnaut
'''

import math as mt
import pygame as pg
pg.init()

def hideWelcome() -> None:
    '''
    Hides the Pygame welcome statement. This statement usually shows Pygame and SDL versions.
    Can be quite annoying in commercial/distributed games.

    Please call this function before importing Pygame.
    '''

    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
    del os

def pointMouse(sprite: pg.sprite.Sprite) -> None:
    '''
    Rotates a sprite's image to point towards the mouse-pointer.

    Args:
        sprite (pg.sprite.Sprite): the sprite that you want to rotate
    '''
    
    mouseX, mouseY = pg.mouse.get_pos()
    
    angleRad = mt.atan2(sprite.rect.centerx - mouseX, sprite.rect.centery - mouseY)
    angle = mt.degrees(angleRad)
    
    if mouseX < sprite.rect.centerx:
        sprite.image = pg.transform.rotate(pg.transform.flip(sprite.image, True, False), angle - 90)
    else:
        sprite.image = pg.transform.rotate(sprite.image, angle + 90)

def center() -> tuple:
    '''
    Returns the center of a Pygame display surface in coordinates.

    Returns:
        centerPos (tuple): the center of the screen as coordinates
    '''
    
    width = pg.display.get_window_size()[0]
    length = pg.display.get_window_size()[1]
    centerPos = (width / 2, length / 2)
    
    return centerPos

def isColliding(sprite: pg.sprite.Sprite, obstacles: pg.sprite.Group | pg.sprite.GroupSingle) -> bool:
    '''
    Checks if any sprites within a Pygame group collide with another sprite.

    Args:
        sprite (pg.sprite.Sprite): the original sprite you want to check for collisions
        obstacles (pg.sprite.Group | pg.sprite.GroupSingle): check if these sprites are colliding with the original sprite

    Returns:
        bool: whether or not any collisions happened with any of the obstacle sprites
    '''
    
    collisions = 0
    
    for obj in obstacles:
        if sprite.rect.collidrect(obj.rect):
            collisions += 1
    
    if collisions >= 1:
        return True
    else:
        return False

def collideTop(sprite: pg.sprite.Sprite, obstacle: pg.sprite.Sprite) -> bool:
    '''
    Checks if an obstacle sprite collides with the top of another sprite.

    Args:
        sprite (pg.sprite.Sprite): the original sprite you want to check for collisions
        obstacle (pg.sprite.Sprite): the sprite that will collide with the original sprite

    Returns:
        bool: if the top of the original sprite collided with the obstacle sprite or not
    '''
    
    sCoords = {
        'topLeft' : sprite.rect.topleft,
        'topRight' : sprite.rect.topright,
        'bottomLeft' : sprite.rect.bottomleft,
        'bottomRight' : sprite.rect.bottomright
    }
    
    oCoords = {
        'topLeft' : obstacle.rect.topleft,
        'topRight' : obstacle.rect.topright,
        'bottomLeft' : obstacle.rect.bottomleft,
        'bottomRight' : obstacle.rect.bottomright
    }
    
    if (sCoords['topLeft'][0] >= oCoords['bottomLeft'][0] and sCoords['topLeft'][0] <= oCoords['bottomRight'][0]) and (sCoords['topLeft'][1] <= oCoords['bottomLeft'][1] and sCoords['topLeft'][1] >= oCoords['topLeft'][1]):
        return True
    
    elif (sCoords['topRight'][0] >= oCoords['bottomLeft'][0] and sCoords['topRight'][0] <= oCoords['bottomRight'][0]) and (sCoords['topRight'][1] <= oCoords['bottomRight'][1] and sCoords['topRight'][1] >= oCoords['topRight'][1]):
        return True
    
    else:
        return False
    
def collideBottom(sprite: pg.sprite.Sprite, obstacle: pg.sprite.Sprite) -> bool:
    '''
    Checks if an obstacle sprite collides with the bottom of another sprite.

    Args:
        sprite (pg.sprite.Sprite): the original sprite you want to check for collisions
        obstacle (pg.sprite.Sprite): the sprite that will collide with the original sprite

    Returns:
        bool: if the bottom of the original sprite collided with the obstacle sprite or not
    '''
    
    sCoords = {
        'topLeft' : sprite.rect.topleft,
        'topRight' : sprite.rect.topright,
        'bottomLeft' : sprite.rect.bottomleft,
        'bottomRight' : sprite.rect.bottomright
    }
    
    oCoords = {
        'topLeft' : obstacle.rect.topleft,
        'topRight' : obstacle.rect.topright,
        'bottomLeft' : obstacle.rect.bottomleft,
        'bottomRight' : obstacle.rect.bottomright
    }

    if (sCoords['bottomLeft'][0] >= oCoords['topLeft'][0] and sCoords['bottomLeft'][0] <= oCoords['topRight'][0]) and (sCoords['bottomLeft'][1] >= oCoords['topLeft'][1] and sCoords['bottomLeft'][1] <= oCoords['bottomLeft'][1]):
        return True
    
    elif (sCoords['bottomRight'][0] >= oCoords['topLeft'][0] and sCoords['bottomRight'][0] <= oCoords['topRight'][0]) and (sCoords['bottomRight'][1] >= oCoords['topRight'][1] and sCoords['bottomRight'][1] <= oCoords['bottomRight'][1]):
        return True
    
    else:
        return False
    
def collideLeft(sprite: pg.sprite.Sprite, obstacle: pg.sprite.Sprite) -> bool:
    '''
    Checks if an obstacle sprite collides with the left of another sprite.

    Args:
        sprite (pg.sprite.Sprite): the original sprite you want to check for collisions
        obstacle (pg.sprite.Sprite): the sprite that will collide with the original sprite

    Returns:
        bool: if the left of the original sprite collided with the obstacle sprite or not
    '''
    
    sCoords = {
        'topLeft' : sprite.rect.topleft,
        'topRight' : sprite.rect.topright,
        'bottomLeft' : sprite.rect.bottomleft,
        'bottomRight' : sprite.rect.bottomright
    }
    
    oCoords = {
        'topLeft' : obstacle.rect.topleft,
        'topRight' : obstacle.rect.topright,
        'bottomLeft' : obstacle.rect.bottomleft,
        'bottomRight' : obstacle.rect.bottomright
    }
    
    if (sCoords['bottomLeft'][0] >= oCoords['bottomLeft'][0] and sCoords['bottomLeft'][0] <= oCoords['bottomRight'][0]) and (sCoords['bottomLeft'][1] <= oCoords['bottomRight'][1] and sCoords['bottomLeft'][1] >= oCoords['topRight'][1]):
        return True
    
    elif (sCoords['topLeft'][0] >= oCoords['topLeft'][0] and sCoords['topLeft'][0] <= oCoords['topRight'][0]) and (sCoords['topLeft'][1] <= oCoords['bottomRight'][1] and sCoords['topLeft'][1] >= oCoords['topRight'][1]):
        return True
    
    else:
        return False

def collideRight(sprite: pg.sprite.Sprite, obstacle: pg.sprite.Sprite) -> bool:
    '''
    Checks if an obstacle sprite collides with the right of another sprite.

    Args:
        sprite (pg.sprite.Sprite): the original sprite you want to check for collisions
        obstacle (pg.sprite.Sprite): the sprite that will collide with the original sprite

    Returns:
        bool: if the right of the original sprite collided with the obstacle sprite or not
    '''
    
    sCoords = {
        'topLeft' : sprite.rect.topleft,
        'topRight' : sprite.rect.topright,
        'bottomLeft' : sprite.rect.bottomleft,
        'bottomRight' : sprite.rect.bottomright
    }
    
    oCoords = {
        'topLeft' : obstacle.rect.topleft,
        'topRight' : obstacle.rect.topright,
        'bottomLeft' : obstacle.rect.bottomleft,
        'bottomRight' : obstacle.rect.bottomright
    }
    
    if (sCoords['bottomRight'][0] >= oCoords['bottomLeft'][0] and sCoords['bottomRight'][0] <= oCoords['bottomRight'][0]) and (sCoords['bottomLeft'][1] <= oCoords['bottomRight'][1] and sCoords['bottomLeft'][1] >= oCoords['topRight'][1]):
        return True
    
    elif (sCoords['topRight'][0] >= oCoords['topLeft'][0] and sCoords['topRight'][0] <= oCoords['topRight'][0]) and (sCoords['topLeft'][1] <= oCoords['bottomRight'][1] and sCoords['topLeft'][1] >= oCoords['topRight'][1]):
        return True
    
    else:
        return False