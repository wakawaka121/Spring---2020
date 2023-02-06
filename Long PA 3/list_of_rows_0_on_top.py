"""
File: list_of_row_0_on_top.py
Author: Derek Tominaga
Purpose: This program contains functions to
that word_search will call to
find the words in a rectangular grid.
Course: CSC 120, spring 2020
"""

def reverse_grid(grid_list):
    """
    This function takes one parameter to reverse the order
    of the inner list that corresponts to grid_list.
    grid_list: is a 2D list that contains the word_search grid.
    reverse_grid: is a 2D list that is returned.
    """
    reversed_grid = []
    for i in grid_list:
        temp_list = i[::-1]
        reversed_grid.append(temp_list)
    return reversed_grid
def print_rect(data):
    """
    This function takes one parameter to print
    the grid in the format of a word serach.
    data: is a list of list
    """
    for i in data:
        string = ""
        for j in i:
            string += j + " "
        print(string)

def read_grid(open_file):
    """
    This function takes one paramenter to read the file
    generates a list of list.
    open_file: is an object information from an
    grid_list: is a 2D list that gets returned.
    """
    grid_list = []
    for lines in open_file:
        info_line = lines.strip("\n").split()
        grid_list.append(info_line)
    return grid_list

def get_wid(grid_list):
    """
    This function takes one parameter to identify
    the width of the word_search grid.
    grid_list: 2D list
    width: is an int value that is returned
    """
    width = len(grid_list[0])
    return width

def get_hei(grid_list):
    """
    This function takes one parameter to identify
    the height of the word_search grid.
    grid_list: 2D list
    height: is an int value that is returned
    """
    height = len(grid_list)
    return height

def read_cell(grid_list, x, y):
    """
    This function takes three parameters to identify
    the character as a specific "coordinate" derived from
    grid_list
    grid_list: a 2D list
    x: is a in value
    y: is an int value
    cell_char: is a string at (x,y), returned
    """
    cell_char = grid_list[y][x]
    return cell_char

def make_dict_bank(dict_file):
    """
    This function takes one parameter to read
    through the file information and make a
    list of strings.
    """
    dict_bank = []
    for lines in dict_file:
        word = lines.strip().lower()
        if word != "" and word[0] !="#":
            dict_bank.append(word)
    return set(dict_bank)





