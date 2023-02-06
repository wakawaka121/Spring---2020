"""
File: list_of_strings.py
Author: Derek Tominaga
Purpose: This program contains fucntions to
build a grid is a list of string. O is oriented
on the top.
It can print and update
the grid aswell.
Course: CSC 120, spring 2020
"""
def add_top_bottom_element(width, j):
    """
    This function takes two parameters to
    generate the top and bottom string
    width: and int value that corresponds to length
    of string
    j: is an int value to determine top or bottom
    """
    strings = ""
    if j == 0:
        for i in range(width):
            if i == 0:
                strings += " "
            elif i < width-1:
                strings += "T"
            elif i == (width -1):
                strings += " "
    else:
        for i in range(width):
            if i == 0:
                strings += " "
            elif i < width-1:
                strings += "B"
            elif i == (width-1):
                strings += " "
    return strings
def build_rect(width, height):
    """
    This function takes two parameters
    to generate a grid of dimensions of
    widthxheight
    width: is an int value
    height: is an int value
    """
    assert width >=3 and height >=3
    list_of_strings = []
    for j in range(height):
        strings = ""
        if j == 0 or j == (height -1):
            top_or_bottom = add_top_bottom_element(width, j)
            list_of_strings.append(top_or_bottom)
        else:
            for i in range(width):
                if i == 0:
                    strings += "L"
                if i < (width-2):
                    strings += "."
                if i == (width -1):
                    strings += "R"
            list_of_strings.append(strings)
    return list_of_strings
def print_rect(data):
    """
    This function takes one parameter to
    print the grid.
    data: is a list of strings
    """
    for i in data:
        print(i)
def update(data, x, y, character):
    """
    This function takes four parameters to update
    an element of the string inside a list.
    data: is a list of strings
    x: is an int value that dictates which x cord
    to change
    y: is an int value that dictates which y cord
    to change
    character: is a string values that gets swaped
    at the x,y cord
    """
    new_string = ""
    for i in range(len(data[y])):
        if i == x:
            new_string += "x"
        else:
            new_string += data[y][i]
    data[y] = new_string