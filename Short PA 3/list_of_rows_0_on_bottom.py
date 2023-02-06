"""
File: list_of_rows_0_on_bottom.py
Author: Derek Tominaga
Purpose: This program contains fucntions to
build a grid from a list of list with 0 on
the bottom.
It can print and update
the grid aswell.
Course: CSC 120, spring 2020
"""

def add_top_bottom_element(width, j, elements):
    """
    This function takes 3 parameters to generate
    the top and bottom elements of the grid.
    width: is an int value that determines number
    of elements in the list
    j: is an int value that determines top or bottom
    elements: is an empty list
    """
    if j == 0:
        for i in range(width):
            if i == 0:
                elements.append(" ")
            elif i < width-1:
                elements.append("B")
            elif i ==  (width -1):
                elements.append(" ")
    else:
        for i in range(width):
            if i == 0:
                elements.append(" ")
            elif i < width-1:
                elements.append("T")
            elif i == (width -1):
                elements.append(" ")
def build_rect(width, height):
    """
    This function takes two parameters to generate
    a grid with dimensions width and height.
    width: is an int value
    height: is an int value
    list_of_elements: gets returned
    """
    assert width >=3 and height >=3
    list_of_elements = []
    for j in range(height):
        elements = []
        if j == 0 or j == (height -1):
            add_top_bottom_element(width, j, elements)
            list_of_elements.append(elements)
        else:
            for i in range(width):
                if i == 0:
                    elements.append("L")
                if i < (width-2):
                    elements.append(".")
                if i == (width -1):
                    elements.append("R")
            list_of_elements.append(elements)
    return list_of_elements
def print_rect(data):
    """
    This function takes one parameter
    to print the grid
    data: is a list of list
    """
    width = len(data[0])
    height = len(data)
    string = ""
    i = 1
    while i <= height:
        for j in data[-i]:
            string += j
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
    data[y][x] = character