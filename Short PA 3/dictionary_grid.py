"""
File: dictionary_grid.py
Author: Derek Tominaga
Purpose: This program contains fucntions to
build a grid where x,y cords are keys of
of the dictionary. It can print and update
the grid aswell.
Course: CSC 120, spring 2020
"""

def add_top_bottom_element(dict_of_elements, width, y):
    """
    This function takes 3 paraments to generate the top
    and bottom of the grid.
    dict_of_elements: is a dictinary of x,y keys
    width: is an int value
    y: is an int value, denotes the y cordinate values
    of the x,y key.
    """
    #when y is 0 build top row
    if y == 0:
        for x in range(width):
            temp_list = []
            if x == 0:
                dict_of_elements[(x,y)] = " "
            elif x < width-1:
                dict_of_elements[(x, y)] = "T"
            else:
                dict_of_elements[(x,y)] = " "
    #when y reaches width build bottom
    else:
        for x in range(width):
            temp_list = []
            if x == 0:
                dict_of_elements[(x,y)] = " "
            elif x < width-1:
                dict_of_elements[(x,y)] = "B"
            else:
                dict_of_elements[(x,y)] = " "
def build_rect(width, height):
    """
    This function takes two paraments to generate
    a grids of specificed height and width
    width: is an int value
    height: is an int value
    dict_of_elements: is returned
    """
    assert width >=3 and height >=3
    dict_of_elements = {}
    for y in range(height):
        if y == 0 or y == height -1:
            add_top_bottom_element(dict_of_elements, width, y)
        else:
            #generates a row, from x,y "coordinates"
            for x in range(width):
                temp_list = []
                if x == 0:
                    dict_of_elements[(x,y)] = "L"
                elif x < width -1:
                    dict_of_elements[(x,y)] = "."
                else:
                    dict_of_elements[(x,y)] = "R"
    return dict_of_elements
def print_rect(data):
    """
    This function takes ones parameter to print
    out the grid.
    data: is a dictionary the x,y tuples as cords
    """
    width_counter = 0
    height_counter = 0
    for values in data.values():
        #used to get width of the grid
        if values == "T":
            width_counter += 1
        #used to get the height of the grid
        if values == "L":
            height_counter +=1
    width_counter += 2
    height_counter += 2
    for y in range(height_counter):
        print_string = ""
        for x in range (width_counter):
            print_string += data[(x,y)]
        print(print_string)
def update(data, x, y, character):
    """
    This function takes four parameters to update
    an element of the list inside a list.
    data: is a dictinary
    x: is an int value that dictates which x cord
    to change
    y: is an int value that dictates which y cord
    to change
    character: is a string values that gets swaped
    at the x,y cord
    """
    data[(x,y)] = character