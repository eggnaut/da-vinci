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

Usage: 'from davinci import data' or 'import davinci.data'

Includes many useful functions related to data and data storage within Python, mainly lists and 2D lists (arrays).

Made by @eggnaut
'''

import random as rd

def isPos(num : float | int) -> bool:
    '''
    CHecks if a data value is positive or equal to 0.
    
    Args:
        num (float | int): the data value you want to check
    
    Returns:
        ans (bool): whether the data value is positive or equal to 0 or not
    '''
    
    return num >= 0

def isInt(num: float | int) -> bool:
    '''
    Checks if a data value is a integer or float.
    
    Args:
        num (float | int): the data value you want to check
        
    Returns:
        ans (bool): whether the data value is a integer or not
    '''
    
    return (num % 1) == 0

def sort(target: list) -> list:
    '''
    Sorts any Python list using the selection sort algorithm.

    Args:
        target (list): any list with any values that needs to be sorted.

    Returns:
        new (list): the same items as the orginal list, but sorted using the selection sort algorithm.
    '''
    
    new = target

    for startIndex in range(len(new)):
        checkList = new[startIndex:]
        lowestIndex = checkList.index(min(checkList)) + startIndex
        new[startIndex], new[lowestIndex] = new[lowestIndex], new[startIndex]

    return new

def generateList(length: int, startVal: int, endVal: int) -> list:
    '''
    Generates a prefilled Python list with random integer items.

    Args:
        length (int): how many items in the list
        startVal (int): the start point for the range of random integers
        endVal (int): the end point for the range of random integers

    Returns:
        new (list): a list with random integer items.
    '''
    new = [rd.randint(startVal, endVal) for i in range(length)]

    return new

def generateArray(rows: int, cols: int, startVal: int, endVal: int) -> list:
    '''
    Generates a prefilled 2D Python list (array) with random integer items.

    Args:
        rows (int): how many rows (lists) you want in the array
        cols (int): how many columns (items) you want in each row (list)
        startVal (int): the start point for the range of random integers
        endVal (int): the end point for the range of random integers

    Returns:
        new (list): a 2D Python list (array) with random integer items.
    '''

    new = []
    for i in range(rows):
        row = [rd.randint(startVal, endVal) for i in range(cols)]
        new.append(row)

    return new

def loopArray(array: list) -> list:
    '''
    Loops through a 2D Python list (array) and finds all items in it.

    Args:
        array (list): the 2D Python list (array) which the function will search through

    Returns:
        cells (list): a list filled with tuples as items. Each tuple follows this format: row (list) index, cell (item) index, cell (item's value)
    '''

    cells = []

    for rowIndex, row in enumerate(array):
        for colIndex, col in enumerate(row):
            cell = (rowIndex, colIndex, col)
            cells.append(cell)

    return cells

def findCell(array: list, cell) -> tuple:
    '''
    Gives the exact coordinates of an item within a 2D Python list (array) in the form of a row index and column index.

    Args:
        array (list): any 2D Python list (array) that contains items with any type of value.
        cell (any): the item you are looking for within the array

    Returns:
        coordinate: the position of the cell within the array as (row index, column index)
    '''

    for rowIndex, row in enumerate(array):
        for colIndex, col in enumerate(row):
            if col == cell:
                break

    coord = (rowIndex, colIndex)
    return coord
