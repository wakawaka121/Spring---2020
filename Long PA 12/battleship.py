"""
File: battleship.py
Author: Derek Tominaga
Description: This program contains
classes and methods that will implement
a one sided game of battle ship.
Course: CSC 120, spring 2020
"""

class Board:
    def __init__(self,size):
        assert size > 0
        self._size = size
        self._grid = self.build_grid(size)
        self.ships = []

    def build_grid(self,size):
        index_list = self.build_y_index(size)
        left_list = self.build_left(size)
        right_list = self.build_right(size)
        board_grid = [index_list, left_list]
        for x in range(size):
            edge_pos = Pos(-1,x)
            edge_pos.status = "--"
            y_list = [edge_pos]
            for y in range(size):
                y_list.append(Pos(x,y))
            y_list.append(edge_pos)
            board_grid.append(y_list)
        board_grid.append(right_list)
        return board_grid

    def build_left(self, size):
        left_end = Pos(-2,0)
        left_end.status = " +"
        y_list = [left_end]
        for y in range(size):
            left_side = Pos(-2,y)
            left_side.status = " |"
            y_list.append(left_side)
        y_list.append(left_end)
        return y_list

    def build_right(self, size):
        right_end = Pos(size+1,0)
        right_end.status = "-+"
        y_list = [right_end]
        for y in range(size):
            right_side = Pos(size+1,y)
            right_side.status = " |"
            y_list.append(right_side)
        y_list.append(right_end)
        return y_list

    def build_y_index(self,size):
        corner = Pos(-3,0)
        corner.status = "  "
        y_list = [corner]
        for y in range(size):
            y_index = Pos(-3,y)
            if len(str(y)) == 1:
                y_index.status = " "+str(y)
                y_list.append(y_index)
            else:
                y_index.status = str(y)
                y_list.append(y_index)
        y_list.append(corner)
        return y_list

    def print(self):
        grid = self._grid
        width = len(grid[0])
        height = len(grid)
        string = ""
        for i in range(width):
            for j in range(height):
                string += str(grid[j][(width-1)-(i)].status)
            print (string)
            string = ""
        self.bottom_index()

    def bottom_index(self):
        bottom_index = [["   "],["   "]]
        for index in range(self._size):
            if len(str(index)) == 1:
                string = " "+str(index)
                bottom_index[0].append(string[0])
                bottom_index[1].append(string[1])
            else:
                string = str(index)
                bottom_index[0].append(string[0])
                bottom_index[1].append(string[1])
        for i in bottom_index:
            index_string = ""
            for j in i:
                index_string += " " + j
            if index_string.strip() != "":
                print (index_string)

    def update(self,pos):
        grid = self._grid
        if grid[pos.x+2][pos.y+1] == " .":
            grid[pos.x+2][pos.y+1] = " o"
        else:
            grid[pos.x+2][pos.y+1] = " *"

    def has_been_used(self,pos):
        assert pos.x < self._size and pos.y < self._size
        grid = self._grid
        if grid[pos.x+2][pos.y+1] not in [" X", " o", " *"]:
            return False
        if grid[pos.x+2][pos.y+1] in [" X", " o", " *"]:
            return True

    def attempt_move(self, pos):
        assert pos.x+2 < self._size and pos.y+1 < self._size
        assert  self.has_been_used(pos) == False
        grid = self._grid
        #print(pos.x,pos.y)
        if grid[pos.x+2][pos.y+1].status == " .":
            grid[pos.x+2][pos.y+1].status = " o"
            Pos(pos.x+2,pos.y+1).status = " o"
            return "Miss"
        else:
            grid[pos.x+2][pos.y+1].status = " *"
            Pos(pos.x+2,pos.y+1).status = " *"
            return "Hit"

    def add_ship(self, ship, position):
        grid = self._grid
        self.ships.append(ship)
        for pos in ship.shape:
            pos.x = pos.x + 2 + position.x
            pos.y = pos.y +1 + position.y
            pos.status = ship.name[0]
            grid[pos.x][pos.y].status = " "+pos.status
class Pos:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.status = " ."

    def rotate(self, rot):
        x = self.x
        y = self.y
        if rot == 1:
            self.x = y
            self.y = -(x)
            return self
        if rot == 2:
            self.x = -(x)
            self.y = -(y)
            return self
        if rot == 3:
            self.x = -(y)
            self.y = x
            return self

class Ship:
    def __init__(self,name,shape):
        self.name = name
        #self.shape = self.ship_dict(shape)
        self.shape = shape

    def is_sunk(self):
        for pos in self.shape:
            if pos.status != " X":
                return False
        return True

    def print(self):
        ship_status = ""
        for pos in self.shape:
            #print(pos.x,pos.y,pos.status)
            ship_status += pos.status
        print (ship_status + " "*(10-len(ship_status))+ self.name )
"""
def main():
    board = Board(20)
    pos = Pos(1,1)
    ship = Ship("Destoryer", [Pos(0,0),Pos(1,0)])
    #ship2 = Ship("Aricraft Carrier", [Pos(0,0),Pos(0,1),Pos(0,2)])
    board.add_ship(ship,pos)
    board.attempt_move(pos)
    print(ship.shape[0].status)
    #board.add_ship(ship2,Pos(0,0))
    #print(board.has_been_used(pos))
    #board.update(pos)
    #print(board.has_been_used(pos))
    #for i in board._grid:
    #    print(len(i),i)
    board.print()
main()
"""