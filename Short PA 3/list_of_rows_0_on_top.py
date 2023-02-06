

def add_top_bottom_element(width, j, elements):
    """
    This function takes 3 parameter add a top
    and bottom of the grid.
    width: is an int value that determines number
    of elements in the list
    j: an int value that determines
    elements: is an empty list
    """
    if j == 0:
        for i in range(width):
            if i == 0:
                elements.append(" ")
            elif i < width-1:
                elements.append("T")
            elif i == (width -1):
                elements.append(" ")
    else:
        for i in range(width):
            if i == 0:
                elements.append(" ")
            elif i < width-1:
                elements.append("B")
            elif i == (width-1):
                elements.append(" ")
def build_rect(width, height):
    """
    This function takes two parameters generate
    the grid with dimensions widthxheight
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
                if i < width-2:
                    elements.append(".")
                if i == (width -1):
                    elements.append("R")
            list_of_elements.append(elements)
    return list_of_elements
def print_rect(data):
    """
    This function takes one parameter to print
    the grid.
    data: is a list of list
    """
    for i in data:
        string = ""
        for j in i:
            string += j
        print(string)
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

def read_grid(open_file):
    """
    This function takes one paramenter to read the file
    generates a list of list.
    open_file: is an object information from an
    """
    grid_list = []
    for lines in open_file:
        info_line = lines.strip("\n").split()
        grid_list.append(info_line)
    return grid_list

def print_grid(grid_list):
    """
    This function takes one parament to print
    the word search
    """
    list_of_rows_0_on_top.print_rect(grid_list)

def get_wid(grid_list):
    width = len(grid_list[0])
    return width

def get_hei(grid_list):
    height = len(grid_list)
    return height

def read_cell(grid_list, x, y):
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
        word = lines.strip()
        word.append(word)
    return set(dict_bank)

def diagonal(word_grid, height, width):
    top_left_bottom_right = []
    bottom_right_top_left = []
    for y in range(height):
        for x in range(width):
            cur_x,cur_y = x,(height-y)
            string_so_far = ""
            while cur_x < width and cur_y < height:
                #cur_char = data_structure.read_cell(word_grid, cur_x, cur_y)
                cur_char = read_cell(word_grid, cur_x, cur_y)
                string_so_far += cur_char
                top_left_bottom_right.append(string_so_far)
                reverse_from_tl_br = string_so_far[::-1]
                bottom_right_top_left.append(reverse_from_tl_br)
                cur_x += 1
                cur_y += 1
    return set(top_left_bottom_right), set(bottom_right_top_left)

def vertical(word_grid, height, width):
    top_bottom_words = []
    bottom_top_words = []
    for y in range(height):
        for x in range(width):
            cur_x,cur_y = x,y
            string_so_far = ""
            while cur_x < width and cur_y < height:
                #cur_char = data_structure.read_cell(word_grid, cur_x, cur_y)
                cur_char = read_cell(word_grid, cur_x, cur_y)
                string_so_far += cur_char
                top_bottom_words.append(string_so_far)
                reverse_from_t_b = string_so_far[::-1]
                bottom_top_words.append(reverse_from_t_b)
                cur_y += 1
    return set(top_bottom_words), set(bottom_top_words)

def horizontal(word_grid, height, width):
    right_left_words = []
    left_right_words = []
    for y in range(height):
        for x in range(width):
            cur_x,cur_y = x,y
            string_so_far = ""
            while cur_x < width and cur_y < height:
                #cur_char = data_structure.read_cell(word_grid, cur_x, cur_y)
                cur_char = read_cell(word_grid, cur_x, cur_y)
                string_so_far += cur_char
                right_left_words.append(string_so_far)
                reverse_from_r_l = string_so_far[::-1]
                left_right_words.append(reverse_from_r_l)
                cur_x += 1
    return set(right_left_words), set(left_right_words)