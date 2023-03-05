import pygame as pg
pg.init()

def coordsDisplay(wn: pg.Surface, 
               sprite: pg.sprite.Sprite,
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
        sprite (pg.sprite.Sprite): A Pygame sprite whose position you want to track.
        fontSize (int | None, optional): Size of the font (Arial). Defaults to 20.
        bold (bool | None, optional): If the text should be bolded. Defaults to False.
        italic (bool | None, optional): If the text should be italicized. Defaults to False.
        pos (tuple | None, optional): The position of the text as a tuple, (x, y). Defaults to (15, 15).
        color (str | tuple, optional): The color of the text. Defaults to '#FFFFFF'.
        bgColor (str | tuple, optional): The background color of the text. Defaults to '#000000'.
    '''
    
    font = pg.font.SysFont('Arial', fontSize, bold, italic)
    coords = sprite.rect.center
    text = font.render(str(coords), True, color, bgColor)
    wn.blit(text, pos)
