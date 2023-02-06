from graphics import *

class Pipes:
    """

    """
    def __init__(self, grid, square_size):
        self._grid = grid
        self._size = square_size
        self._wid = len(grid[0])
        self._hei = len(grid)

    def get_wid(self):
        return self._wid

    def get_hei(self):
        return self._hei

    def get_square_size(self):
        return self._size

    def set_square_size(self,new_val):
        self._size = new_val

    def set_fill_state(self, x,y, state):

    def rotate_cw(self, x, y):

    def rotate_ccw(self, x, y):

    def get_cell(self, x, y):

class Room:
    """
    """
    def __init__(self):