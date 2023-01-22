'''
Part of EggEngine.

Usage: 'from EggEngine import entities' or 'import EggEngine.entities'

Useful functions and classes for entities, mainly collisions between Pygame sprites.

Made by @eggnaut
'''

import pygame as pg
pg.init()

def isColliding(sprite: pg.sprite.Sprite, obstacles: pg.sprite.Group | pg.sprite.GroupSingle) -> bool:
    collisions = 0
    
    for obj in obstacles:
        if sprite.rect.collidrect(obj.rect):
            collisions += 1
    
    if collisions >= 1:
        return True
    else:
        return False

def collideTop(sprite: pg.sprite.Sprite, obstacle: pg.sprite.Sprite) -> bool:
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