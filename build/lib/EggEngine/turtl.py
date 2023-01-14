'''
Part of EggEngine.

Usage: 'from EggEngine import turtl' or 'import EggEngine.turtl'

Includes functions for drawing custom shapes/polygons with customizability and ease. Utilizes Turtle from turtle module.

Made by @eggnaut.
'''

import turtle as tl

def drawPolygon(length: int, sides: int, color: str | tuple, fillColor: str | tuple | None = None, fill: bool | None = False, penWidth: int | None = 0, pos: tuple | None = (0, 0)) -> None:
    '''
    Draws a regular polygon with as many sides wanted with some customization.

    Args:
        length (int): length of each side
        sides (int): number of sides
        color (str | tuple): color of sides
        fillColor (str | tuple | None, optional): the color used to fill the shape. defaults to None
        fill (bool | None, optional): if you want to fill the shape with color. defaults to False.
        penWidth (int | None, optional): thickness of each side. defaults to 0.
        pos (tuple | None, optional): where the shape should be dawn at. defaults to (0, 0).
    '''
    
    turtleObj = tl.Turtle()
    turtleObj.color(color)
    turtleObj.width(penWidth)
    turtleObj.fillcolor(fillColor)
    turtleObj.penup()
    turtleObj.goto(pos)
    angle = 180 - ((180 * (sides - 2)) / sides)
    turtleObj.pendown()

    if fill:
        turtleObj.begin_fill()

    for i in range(sides):
        turtleObj.fd(length)
        turtleObj.rt(angle)

    turtleObj.end_fill()
    turtleObj.penup()

def drawRect(width: int, length: int, color: str | tuple, fillColor: str | tuple | None = None, fill: bool | None = False, penWidth: int | None = 0, pos: tuple | None = (0, 0)) -> None:
    '''
    Draws a simple rectangle with some customization.

    Args:
        width (int): width of the rectangle horizontally
        length (int): length of the rectangle vertically
        color (str | tuple): color of each side
        fillColor (str | None): the color the rectangle will be filled with. defaults to None
        fill (bool | None, optional): if you want to fill the rectangle with color. defaults to False.
        penWidth (int | None, optional): thickness of each side. defaults to 0.
        pos (tuple | None, optional): where the rectangle should be drawn at. defaults to (0, 0).
    '''
    
    turtleObj = tl.Turtle()
    turtleObj.color(color)
    turtleObj.width(penWidth)
    turtleObj.fillcolor(fillColor)
    turtleObj.penup()
    turtleObj.goto(pos)
    angle = 270
    turtleObj.pendown()

    if fill:
        turtleObj.begin_fill()

    for i in range(2):
        turtleObj.fd(width)
        turtleObj.rt(angle)
        turtleObj.fd(length)
        turtleObj.rt(angle)

    turtleObj.end_fill()
    turtleObj.penup()