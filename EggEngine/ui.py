'''
Part of EggEngine.

Usage: 'from EggEngine import ui' or 'import EggEngine.ui'

Useful and basic UI elements which currently include buttons with support for animations.

Made by @eggnaut
'''

import sys
import pygame as pg
pg.init()

class button(pg.sprite.Sprite):
    '''
    A base class to make animated, hoverable and clickable buttons.
    
    You need to program the on-click actions for each button yourself.
    '''
    def __init__(self, imagePath: str | None, frames: list | None = None, hoverEffect: str | None = 'brighten', pos: tuple = (0, 0)):
        super().__init__()
        
        if imagePath and not frames:
            self.anim = False
            self.normal = pg.image.load(imagePath)
            if hoverEffect == 'brighten':
                self.hover = self.image.fill((150, 150, 150), special_flags = pg.BLEND_RGB_ADD)
            elif hoverEffect == 'darken':
                self.hover = self.image.fill((150, 150, 150), special_flags = pg.BLEND_RGB_SUB)
            self.image = self.normal
        elif not imagePath and frames:
            self.anim = True
            self.frames = [pg.image.load(path) for path in frames]
            if self.hoverEffect == 'brighten':
                self.hovers =  [image.fill((150, 150, 150), special_flags = pg.BLEND_RGB_ADD) for image in self.frames]
            elif hoverEffect == 'darken':
                self.hovers =  [image.fill((150, 150, 150), special_flags = pg.BLEND_RGB_SUB) for image in self.frames]
            self.frameIndex = 0
            self.image = self.frames[self.frameIndex]
            
        self.quit = quit
        self.pos = pos
    
    def onHover(self):
        mousePos = pg.mouse.get_pos()
        
        if self.rect.collidepoint(mousePos):
            if self.anim:
                self.image = self.hovers[self.frameIndex]
            else:
                self.image = self.hover
        else:
            if self.anim:
                self.image = self.frames[self.frameIndex]
            else:
                self.image = self.normal
        
    def update(self):
        if self.anim:
            self.frameIndex += 0.1
            if self.frameIndex > (len(self.frames) - 1):
                self.frameIndex = 0

        self.onHover()
        
class quitButton(button):
    '''
    A basic button that, when clicked, exits the program.
    '''
    
    def __init__(self, imagePath: str | None, frames: list | None = None, hoverEffect: str | None = 'brighten', pos: tuple = (0, 0)):
        super().__init__(imagePath, frames, hoverEffect, pos)
        
    def onClick(self):
        mousePos = pg.mouse.get_pos()
        if self.rect.collidepoint(mousePos):
            if pg.mouse.get_pressed()[0]:
                sys.exit()
        
    def update(self):
        pass