"""
File: one_big_string.py
Author: Derek Tominaga
Purpose: This program contains fucntions to
build a grid from one long string. 0 is
oriented on the top.
It can print and update
the grid aswell.
Course: CSC 120, spring 2020
"""

def add_top_bottom_element(width, j):
    """
    This function takes two parameters to
    generate the top and bottoms of
    the grid.
    width: is an int value that determines how
    long the "string" between the new lines
    caracter is.
    j: is an int value that determines top or bottom
    """
    string = " "
    if j == 0:
        for i in range(width-1):
                if i < width-2:
                    string += "T"
                else:
                    string += " \n"
    else:
        for i in range(width-1):
            if i < width-2:
                string += "B"
            else:
                string += " \n"
    return string
def build_rect(width, height):
    """
    This function takes two parameters to
    generate a grid with dimensions widthxheight
    width: is an int value
    height: is an int value
    one_string: is a string that gets returned
    """
    assert width >=3 and height >=3
    one_string = ""
    for i in range (height):
        if i == 0 or i == height-1:
            string = add_top_bottom_element(width, i)
            one_string += string
        else:
            row_string = ""
            for i in range(width):
                if i == 0:
                    row_string += "L"
                elif i < width-1:
                    row_string += "."
                else:
                    row_string += "R\n"
            one_string += row_string
    return one_string
def print_rect(data):
    """
    prints the grid from that data
    data: is one long string
    """
    print(data)
def update(data, x, y, character):
    """
    This function takes four parameters to update
    an element of the list inside a list.
    data: is a list of list
    x: is an int value that dictates which "x cord"
    to change
    y: is an int value that dictates which "y cord"
    to change
    character: is a string values that gets swaped
    at the x,y cord
    """
    updated_string = ""
    list_for_info = data.split("\n")
    width = len(list_for_info[0])
    #range to character to be changed
    first_cut = (width*y + x) + y
    updated_string += data[:first_cut]
    updated_string += character
    updated_string += data[first_cut+1:]
    return updated_string