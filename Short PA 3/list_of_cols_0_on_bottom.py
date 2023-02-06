"""
File: list_of_col_0_on_bottom.py
Author: Derek Tominaga
Purpose: This program contains fucntions to
build a grid from a list of list. Oriented
with the y-cord 0 is at the bottom left
Course: CSC 120, spring 2020
"""

def add_side_element(height, j, elements):
    """
    This fucntion takes 3 parameters to build
    the side of the grid.
    height: is an int value of number of elements
    in the list
    j: is an int value that denotes the top
    or bottom
    elements: is a an empty list that is filled
    """
    #generates left side of the grid
    if j == 0:
        for i in range(height):
            if i == 0:
                elements.append(" ")
            elif i < height-1:
                elements.append("L")
            else:
                elements.append(" ")
    #generates the right side of the grid
    else:
        for i in range(height):
            if i == 0:
                elements.append(" ")
            elif i < height-1:
                elements.append("R")
            else:
                elements.append(" ")
def build_rect(width, height):
    """
    This fucntion takes two parameters to generate
    the grid as a list of list
    width: is an int value denoting number of list
    height: is an int value denoting number of elements
    in the list
    """
    assert width >=3 and height >=3
    list_of_elements = []
    for j in range(width):
        elements = []
        if j == 0 or j ==(width-1):
            add_side_element(height, j, elements)
            list_of_elements.append(elements)
        else:
            for i in range(height):
                if i == 0:
                    elements.append("B")
                elif i < height-1:
                    elements.append(".")
                else:
                    elements.append("T")
            list_of_elements.append(elements)
    return list_of_elements
def print_rect(data):
    """
    This fucntion takes one parameter to print
    the grid from list of list.
    data: is a list of list
    """
    height = len(data[0])
    width = len(data)
    string = ""
    for j in range(height):
        for i in range(width):
            string += data[i][(height-1)-j]
        print(string)
        string = ""
def update(data, x, y, character):
    """
    This function takes four parameters to update
    an element of the list inside a list.
    data: is a list of list
    x: is an int value that dictates which x cord
    to change
    y: is an int value that dictates which y cord
    to change
    character: is a string values that gets swaped
    at the x,y cord
    """
    data[x][y] = character