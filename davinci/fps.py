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
