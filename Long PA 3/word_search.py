
"""
File: word_search.py
Author: Derek Tominaga
Purpose: This program runs a main; opens a files
and passes the open files as objects.
It will logically call the functions required to
search for words from a word bank and a character
grid.
Course: CSC 120, spring 2020
"""

from list_of_rows_0_on_top import *

def diagonal_tright_to_bleft(grid_list, dict_bank):
    """
    This function takes two parameters to scan
    through the grid with a particular algorithm.
    It idendifies all possible combinations of strings
    in the diagonal direction top right to bottom left.
    grid_list: 2D list that is scanned
    dict_bank: is a set of strings.
    """
    #reverses grid to maintain logic from diagonal top left to
    ##bottom right
    reversed_grid = reverse_grid(grid_list)
    top_right_bottom_left_words = []
    bottom_left_top_right_words = []
    height =  get_hei(grid_list)
    width = get_wid(grid_list)
    for y in range(height):
        for x in range(width):
            cur_x,cur_y = x, y
            string_so_far = ""
            while cur_x < width and cur_y < height:
                char_here = read_cell(reversed_grid, cur_x, cur_y)
                string_so_far += char_here
                top_right_bottom_left_words.append(string_so_far)
                #tr is top righth to bottom left
                #reverses string to check reverse relative direction
                reverse_from_tr = string_so_far[::-1]
                bottom_left_top_right_words.append(reverse_from_tr)
                cur_x += 1
                cur_y += 1
    #gets words that exists in dict_bank set and word set
    diag_bl_tr = sorted(set(bottom_left_top_right_words)&dict_bank)
    diag_tr_bl = sorted(set(top_right_bottom_left_words)&dict_bank)
    if len(diag_bl_tr) != 0:
        print((", ").join(diag_bl_tr), "(diagonal, bottom-left to top-right)")
    if len(diag_tr_bl) !=0:
        print((", ").join(diag_tr_bl), "(diagonal, top-right to bottom-left)")

def diagonal_tleft_to_bright(grid_list, dict_bank):
    """
    This function takes two parameters to scan
    through the grid with a particular algorithm.
    It idendifies all possible combinations of strings
    in the diagonal direction top left to bottom right.
    grid_list: 2D list that is scanned
    dict_bank: is a set of strings.
    """
    top_left_bottom_right_words = []
    bottom_right_top_left_words = []
    height =  get_hei(grid_list)
    width = get_wid(grid_list)
    for y in range(height):
        for x in range(width):
            cur_x,cur_y = x, y
            string_so_far = ""
            while cur_x < width and cur_y < height:
                char_here = read_cell(grid_list, cur_x, cur_y)
                string_so_far += char_here
                top_left_bottom_right_words.append(string_so_far)
                #tl is top left to bottom right
                #reverses string to check reverse relative direction
                reverse_from_tl = string_so_far[::-1]
                bottom_right_top_left_words.append(reverse_from_tl)
                cur_x += 1
                cur_y += 1
    #gets words that exists in dict_bank set and word set
    diag_tl_br = sorted(set(top_left_bottom_right_words)&dict_bank)
    diag_br_tl = sorted(set(bottom_right_top_left_words)&dict_bank)
    if len(diag_tl_br) != 0:
        print((", ").join(diag_tl_br), "(diagonal, top-left to bottom-right)")
    if len(diag_br_tl) !=0:
        print((", ").join(diag_br_tl), "(diagonal, bottom-right to top-left)")

def vertical(grid_list, dict_bank):
    """
    This function takes two parameters to scan
    through the grid with a particular algorithm.
    It idendifies all possible combinations of strings
    in the vertical direction.
    grid_list: 2D list that is scanned
    dict_bank: is a set of strings.
    """
    top_bottom_words = []
    bottom_top_words = []
    height =  get_hei(grid_list)
    width = get_wid(grid_list)
    for y in range(height):
        for x in range(width):
            cur_x,cur_y = x,y
            string_so_far = ""
            while cur_x < width and cur_y < height:
                char_here = read_cell(grid_list, cur_x, cur_y)
                string_so_far += char_here
                top_bottom_words.append(string_so_far)
                #tb is "top bottom"
                #reverses string to check reverse relative direction
                reverse_from_tb = string_so_far[::-1]
                bottom_top_words.append(reverse_from_tb)
                cur_y += 1
    #gets words that exists in dict_bank set and word set
    vertical_tb = sorted(set(top_bottom_words)&dict_bank)
    vertical_bt = sorted(set(bottom_top_words)&dict_bank)
    if len(vertical_tb) != 0:
        print((", ").join(vertical_tb), "(vertical, top-to-bottom)")
    if len(vertical_bt) !=0:
        print((", ").join(vertical_bt), "(vertical, bottom-to-top)")

def horizontal(grid_list, dict_bank):
    """
    This function takes two parameters to scan
    through the grid with a particular algorithm.
    It idendifies all possible combinations of strings
    in the horizonal direction.
    grid_list: 2D list that is scanned
    dict_bank: is a set of strings.
    """
    left_right_words = []
    right_left_words = []
    height =  get_hei(grid_list)
    width = get_wid(grid_list)
    for y in range(height):
        for x in range(width):
            cur_x,cur_y = x,y
            string_so_far = ""
            while cur_x < width and cur_y < height:
                char_here = read_cell(grid_list, cur_x, cur_y)
                string_so_far += char_here
                left_right_words.append(string_so_far)
                #rl is "right left"
                #reverses string to check reverse relative direction
                reverse_from_rl = string_so_far[::-1]
                right_left_words.append(reverse_from_rl)
                cur_x += 1
    #gets words that exists in dict_bank set and word set
    horizontal_lr = sorted(set(left_right_words)&dict_bank)
    horizontal_rl = sorted(set(right_left_words)&dict_bank)
    if len(horizontal_lr) != 0:
        print((", ").join(horizontal_lr), "(horizontal, L-to-R)")
    if len(horizontal_rl) != 0:
        print((", ").join(horizontal_rl), "(horizontal, R-to-L)")

def open_file():
    """
    This function take no parameter but will promnpt for
    user input and open the file then return the file as an
    object.
    """
    opened_file = open(input(), "r")
    return opened_file
def main():
    dict_data = open_file()
    dict_bank_set = make_dict_bank(dict_data)
    opened_file = open_file()
    word_grid = read_grid(opened_file)
    height = get_hei(word_grid)
    width = get_wid(word_grid)
    print(len(dict_bank_set), "words read from the dictionary.")
    print("Grid read. " + " wid=" + str(width) + " hei=" + str(height))
    print_rect(word_grid)
    horizontal(word_grid, dict_bank_set)
    vertical(word_grid, dict_bank_set)
    diagonal_tleft_to_bright(word_grid, dict_bank_set)
    diagonal_tright_to_bleft(word_grid, dict_bank_set)

if __name__ == "__main__":
    main()