"""
File: pipegrid.py
Author: Derek Tominaga
Description: This program works with 3 classes.
to draw a grid of squares with "pipes" in the
square cells.
Pipes class makes an object with informaton about the grid
Cell class makes an object with information about a cell.
SquareDrawing makes a graphics object cell, that gets drawn
with "pipes" in it.
Course: CSC 120, spring 2020
"""

from graphics import *

class Pipes:
    """
    This class represents a pipe grid. It can contain
    any number of cells in a quadrilater shape with possible
    connections in the NESW "directions" a special case and a
    fill satus.

    The constructor will build a list of objects, which are can be
    considered a "cell" with NESW directions, Special Case and fill
    status.
    """

    def __init__(self, grid, square_size):
        """
        This is the constructor that takes two parameters to
        build a list of objects that are cells.
        grid: is a list of strings that is used to
        build a list of cell objects.
        square_size: is an int value that represents the width
        of a cell.
        """
        assert square_size > 0
        self._size = square_size
        self._rooms = Cell.build_grid(len(grid[0]),len(grid),grid)
        self._wid = len(grid[0])
        self._hei = len(grid)

    def draw(self):
        """
        This method takes no parameter in-order
        to draw the pipe grid. It will call for information
        from another class object.
        """
        wid = self.get_wid()
        hei = self.get_hei()
        list_of_rooms = self._rooms
        dimensions = self.get_square_size()
        #creates graphics object with dimensions based on how big each cell is
        ## and how many cells horizontally and vertically there are
        gui = graphics(dimensions*wid, dimensions*hei, "Pipe Grid")
        for row in range(len(list_of_rooms)):
            for col in range(len(list_of_rooms)):
                #creates a square object that represent a cell
                print_square = SquareDrawing(gui, dimensions, row*dimensions, col*dimensions)
                #assign the "pipe" attributes that belong to a a cell at a specific
                ##row and column
                print_square = SquareDrawing.pipe_layout(print_square,
                    self.list_cell_info(row,col), row, col)
        #formatting loop, adds the grid lines.
        y_pos = 0
        x_pos = 0
        while y_pos <= dimensions*hei:
            gui.line(0 ,y_pos , wid*dimensions, y_pos, "white", 3)
            gui.line(x_pos, 0, x_pos, hei*dimensions, "white", 3)
            y_pos += dimensions
            x_pos += dimensions
        gui.mainloop()

    def get_wid(self):
        """
        This method gets and returns the
        width of the grid. The width is the
        number of cells horrizontally.
        """
        return self._wid

    def get_hei(self):
        """
        This method gets and returns the
        height of the grid. The height is the
        number of cells vertically.
        """
        return self._hei

    def get_square_size(self):
        """
        This method gets and returns the width
        that each "cell" object should be.
        """
        return self._size

    def set_square_size(self,new_val):
        """
        This method will take one parameter to
        and will change the square_size attribute
        """
        self._size = new_val

    def set_fill_state(self, x, y, state):
        """
        This method takes three parameters in-order to
        set the "fill state" of a particual cell object.
        The orientation of the grid is from the top left.
        x: is an int value that represents the x-cord which
        is the "innner element" of a 2D list.
        y: is an int value that represents the y-cord which
        is the "outter element" of a 2D list.
        state: is a bool value that sets the fill state of a cell.
        """
        self._rooms[y][x].f = state

    def rotate_cw(self, x, y):
        """
        This method takes two parameters to rotate
        a cell clockwise direction
        The orientation of the grid is from the top left.
        x: is an int value that represents the x-cord which
        is the "innner element" of a 2D list.
        y: is an int value that represents the y-cord which
        is the "outter element" of a 2D list.
        """
        cell_info = self.list_cell_info(x,y)
        reset_info = [False,False,False,False]
        for element in range(len(reset_info)):
            #1 is index of east info
            if cell_info[element] is True and element == 0:
                reset_info[1] = True
            #2 is index of north info
            if cell_info[element] is True and element ==1:
                reset_info[2] = True
            #3 is index of east info
            if cell_info[element] is True and element == 2:
                reset_info[3] = True
            #0 is index of south info
            if cell_info[element] is True and element == 3:
                reset_info[3] = True
        self._rooms[y][x].n = reset_info[0]
        self._rooms[y][x].e = reset_info[1]
        self._rooms[y][x].s = reset_info[2]
        self._rooms[y][x].w = reset_info[3]

    def rotate_ccw(self, x, y):
        """
        This method takes two parameters to rotate
        a cell counter-clockwise direction.
        The orientation of the grid is from the top left.
        x: is an int value that represents the x-cord which
        is the "innner element" of a 2D list.
        y: is an int value that represents the y-cord which
        is the "outter element" of a 2D list.
        """
        cell_info = self.list_cell_info(x,y)
        reset_info = [False,False,False,False]
        for element in range(len(reset_info)):
            if cell_info[element] is True and element == 0:
                #3 is index of west
                reset_info[3] = True
            if cell_info[element] is True and element == 1:
                #0 is index of north
                reset_info[0] = True
            if cell_info[element] is True and element == 2:
                #1 is index of east
                reset_info[1] = True
            if cell_info[element] is True and element == 3:
                #2 is index of south
                reset_info[2] = True
        self._rooms[y][x].n = reset_info[0]
        self._rooms[y][x].e = reset_info[1]
        self._rooms[y][x].s = reset_info[2]
        self._rooms[y][x].w = reset_info[3]

    def get_cell(self, x, y):
        """
        This method takes two parameters inorder to return
        the string that contains the information about a cell.
        ex "nesw+(f)"
        The orientation of the grid is from the top left.
        x: is an int value that represents the x-cord which
        is the "innner element" of a 2D list.
        y: is an int value that represents the y-cord which
        is the "outter element" of a 2D list.
        """
        cell_info = self.list_cell_info(x,y)
        character_list = ["n","e","s","w","+","(f)"]
        current_state = ""
        for element in range(len(cell_info)):
            if cell_info[element] is True:
                current_state += character_list[element]
        return current_state

    def list_cell_info(self, x, y):
        """
        This method takes two parameters to create a
        list that contains bool values about a specific
        cell.
        The orientation of the grid is from the top left.
        x: is an int value that represents the x-cord which
        is the "innner element" of a 2D list.
        y: is an int value that represents the y-cord which
        is the "outter element" of a 2D list.
        return: room_list_info, a list of bools that
        contains specific cell info.
        """
        room_list_info = []
        room_list_info.append(self._rooms[y][x].n)
        room_list_info.append(self._rooms[y][x].e)
        room_list_info.append(self._rooms[y][x].s)
        room_list_info.append(self._rooms[y][x].w)
        room_list_info.append(self._rooms[y][x].p)
        room_list_info.append(self._rooms[y][x].f)
        return room_list_info


class SquareDrawing:
    """
    This class is used to create a graphics object.
    This object is a square of a specific width,
    and will get the "pipe" attributes "drawn" on the
    square graphics object.
    """

    def __init__(self, gui, width, row, col):
        """
        This is a constructor that takes four parameters
        to create a square graphics object with public attributes
        gui: is a graphics object
        width: is the size the square graphics object should be
        row: is an int value, it is one of two values that designates
        where in the gui canvas the square graphics object will be drawn
        col: is an int value, it is one of two values that designates
        where in the gui canvas the square graphics object will be drawn.
        """
        self.size = width
        self.main = gui
        #width, width is used for both the height and width since it is
        ##represent a square
        self.container = gui.rectangle(row, col, width, width, "grey")
        self.p = None
        self.n = None
        self.e = None
        self.s = None
        self.w = None

    def north(self, row, col, state):
        """
        This method takes 3 parameters to draw
        the "pipe" in the northern direction. On the square
        graphics object.
        row: is an int value that represents the x-cord of the
        cell
        col: is an int value that represents the y-cord of the
        cell
        state: is a bool value that represents the fill state
        """
        #is the width or height of the cell square
        dimensions = self.size
        #off set to place square object in approiate position
        ## in the canvas object(gui)
        row_off_set = dimensions*row + dimensions/2.25
        col_off_set = dimensions*col
        if state is False:
            self.n = self.main.rectangle(row_off_set, col_off_set,
                dimensions/15, dimensions/2, "black")
        else:
            self.n = self.main.rectangle(row_off_set, col_off_set,
                dimensions/15, dimensions/2, "green")

    def east(self, row, col, state):
        """
        This method takes 3 parameters to draw
        the "pipe" in the eastern direction. On the square
        graphics object.
        row: is an int value that represents the x-cord of the
        cell
        col: is an int value that represents the y-cord of the
        cell
        state: is a bool value that represents the fill state
        """
        dimensions = self.size
        row_off_set = dimensions*row + dimensions/2
        col_off_set = dimensions*col + dimensions/2.3
        if state is False:
            self.e = self.main.rectangle(row_off_set, col_off_set,
                dimensions/2, dimensions/15, "black")
        else:
            self.e = self.main.rectangle(row_off_set, col_off_set,
                dimensions/2, dimensions/15, "green")

    def south(self,row, col, state):
        """
        This method takes 3 parameters to draw
        the "pipe" in the southern direction. On the square
        graphics object.
        row: is an int value that represents the x-cord of the
        cell
        col: is an int value that represents the y-cord of the
        cell
        state: is a bool value that represents the fill state
        """
        dimensions = self.size
        row_off_set = dimensions*row + dimensions/2.25
        col_off_set = dimensions*col + dimensions/2.3
        if state is False:
            self.s = self.main.rectangle(row_off_set, col_off_set,
                dimensions/15, dimensions/1.5, "black")
        else:
            self.s = self.main.rectangle(row_off_set, col_off_set,
                dimensions/15, dimensions/1.5, "green")

    def west(self, row, col, state):
        """
        This method takes 3 parameters to draw
        the "pipe" in the western direction. On the square
        graphics object.
        row: is an int value that represents the x-cord of the
        cell
        col: is an int value that represents the y-cord of the
        cell
        state: is a bool value that represents the fill state
        """
        dimensions = self.size
        row_off_set = dimensions*row
        col_off_set = dimensions*col + dimensions/2.3
        if state is False:
            self.w = self.main.rectangle(row_off_set, col_off_set,
                dimensions/2, dimensions/15, "black")
        else:
            self.w = self.main.rectangle(row_off_set, col_off_set,
                dimensions/2, dimensions/15, "green")

    def pool(self, row, col, state):
        """
        This method takes 3 parameters to draw
        the "pipe" special case. On the square
        graphics object.
        row: is an int value that represents the x-cord of the
        cell
        col: is an int value that represents the y-cord of the
        cell
        state: is a bool value that represents the fill state
        """
        dimensions = self.size
        row_off_set = dimensions*row + dimensions/2.15
        col_off_set = dimensions*col + dimensions/2.1
        if state is False:
            self.p = self.main.ellipse(row_off_set, col_off_set, 20, 20, "black")
        else:
            self.p = self.main.ellipse(row_off_set, col_off_set, 20, 20, "green")

    def pipe_layout(self, cell_info, row, col):
        """
        This method takes 3 parameters to put the pipe
        layout on the the square graphics object.
        cell_info: is a list of cell attributes
        row: is an int value that represents the x-cord of the
        cell
        col: is an int value that represents the y-cord of the
        cell
        """
        cell_info = cell_info
        for index in range(len(cell_info)):
            if cell_info[index] == True and index == 0:
                self.north(row, col, cell_info[5])
            if cell_info[index] == True and index == 1:
                self.east(row, col, cell_info[5])
            if cell_info[index] == True and index == 2:
                self.south(row, col, cell_info[5])
            if cell_info[index] == True and index == 3:
                self.west(row, col, cell_info[5])
            if cell_info[index] == True and index == 4:
                self.pool(row, col, cell_info[5])

class Cell:
    """
    This class represents a cell it can contains
    bool values indicating if the cell has a
    NESW direction, a Special condition and the
    fill condition is initially set to False.
    """

    def __init__(self):
        """
        This is the constructor, the NESW directions are
        default set to False and will be changed based on
        what string contained in the grid.
        """
        self.n = False
        self.e = False
        self.s = False
        self.w = False
        self.p = False
        self.f = False

    def build_grid(wid,hei,grid):
        """
        This method takes 3 parameters to build a 2D list of cell
        objects. All the objects attributes are default set to False.
        wid: is an int value that represents number of cells in a row.
        hei: is an int value that represents number of cells in a column.
        grid: is a 2D list of strings
        return: a 2d list of cell objects
        """
        assert wid >= 1 and hei >=1
        list_of_cells = []
        count = 0
        for row in range(hei):
            elements = []
            for cell in range(wid):
                elements.append(Cell())
            list_of_cells.append(elements)
        return Cell.link_cells(list_of_cells, grid)

    def link_cells(list_of_cells, grid):
        """
        This method takes two parameters to assign the
        cells attributes based on the string contained
        in the grid, which is a 2D list.
        list_of_cells: is a list of cell objects
        grid: is a 2D list of strings that that determine
        cells attributes.
        return: list_of_cells is a list of cell objects
        """
        wid = len(grid[0])
        hei = len(grid)
        for row in range(hei):
            for cell in range(wid):
                for index in range(len(grid[row][cell])):
                    if grid[row][cell][index] == "n":
                        list_of_cells[row][cell].n = True
                    if grid[row][cell][index] == "e":
                        list_of_cells[row][cell].e = True
                    if grid[row][cell][index] == "s":
                        list_of_cells[row][cell].s = True
                    if grid[row][cell][index] == "w":
                        list_of_cells[row][cell].w = True
                    if grid[row][cell][index] == "+":
                        list_of_cells[row][cell].p = True
        return list_of_cells