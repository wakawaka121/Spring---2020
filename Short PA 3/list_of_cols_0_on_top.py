"""
File: list_of_cols_0_on_top.py
Author: Derek Tominaga
Purpose: This program contains fucntions to
build a grid is a list of list. 0 is oriented at
the top.
It can print and update
the grid aswell.
Course: CSC 120, spring 2020
"""

def add_side_element(height, j, elements):
    """
    This function takes 3 paramets to build the list
    that is the side of the grid.
    height: is an int value that is number of elements
    in the list
    elements: is an empty list
    """
    if j == 0:
        for i in range(height):
            if i == 0:
                elements.append(" ")
            elif i < height-1:
                elements.append("L")
            else:
                elements.append(" ")
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
    This function takes two parameters to build
    a grid of specified width and height
    width: is an int value
    height: is an int value
    list_of_elements: gets returned
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
                    elements.append("T")
                elif i < height-1:
                    elements.append(".")
                else:
                    elements.append("B")
            list_of_elements.append(elements)
    return list_of_elements
def print_rect(data):
    """
    This function takes one parameter to
    print out the grid from the data
    data: is a list of list
    """
    string = ""
    j = 0
    for j in range(len(data[j])):
        i = 0
        while i in range(len(data)):
            string += data[i][j]
            i += 1
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