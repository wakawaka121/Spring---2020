"""
File: prob3.py
Author: Derek Tominaga
Purpose: This program contains functions,
classes, and methods to generate a "grid"
maze of objects
Course: CSC 120, spring 2020
"""

def link_top_row(list_of_rooms, i, j):
    if j == 0:
        list_of_rooms[i][j].e = list_of_rooms[i][j+1]
        list_of_rooms[i][j].s = list_of_rooms[i+1][j]
    elif j < len(list_of_rooms[i])-1:
        list_of_rooms[i][j].e = list_of_rooms[i][j+1]
        list_of_rooms[i][j].w = list_of_rooms[i][j-1]
        list_of_rooms[i][j].s = list_of_rooms[i+1][j]
    elif j == (len(list_of_rooms[i])-1):
        list_of_rooms[i][j].w = list_of_rooms[i][j-1]
        list_of_rooms[i][j].s = list_of_rooms[i+1][j]

def link_mid_rows(list_of_rooms, i, j):
    if j == 0:
        list_of_rooms[i][j].n = list_of_rooms[i-1][j]
        list_of_rooms[i][j].e = list_of_rooms[i][j+1]
        list_of_rooms[i][j].s = list_of_rooms[i+1][j]
    elif j < len(list_of_rooms[i])-1:
        list_of_rooms[i][j].n = list_of_rooms[i-1][j]
        list_of_rooms[i][j].e = list_of_rooms[i][j+1]
        list_of_rooms[i][j].s = list_of_rooms[i+1][j]
        list_of_rooms[i][j].w = list_of_rooms[i][j-1]
    elif j == (len(list_of_rooms[i])-1):
        list_of_rooms[i][j].n = list_of_rooms[i-1][j]
        list_of_rooms[i][j].s = list_of_rooms[i+1][j]
        list_of_rooms[i][j].w = list_of_rooms[i][j-1]

def link_bottom_rows(list_of_rooms, i , j):
    if j == 0:
        list_of_rooms[i][j].n = list_of_rooms[i-1][j]
        list_of_rooms[i][j].e = list_of_rooms[i][j+1]
    elif j < len(list_of_rooms[i])-1:
        list_of_rooms[i][j].n = list_of_rooms[i-1][j]
        list_of_rooms[i][j].e = list_of_rooms[i][j+1]
        list_of_rooms[i][j].w = list_of_rooms[i][j-1]
    else:
        list_of_rooms[i][j].n = list_of_rooms[i-1][j]
        list_of_rooms[i][j].w = list_of_rooms[i][j-1]

def build_grid(wid,hei):
    assert wid >= 1 and hei >=1
    list_of_rooms = []
    count = 0
    for i in range(hei):
        elements = []
        for j in range(wid):
            elements.append(Room(str(count)))
            count += 1
        list_of_rooms.append(elements)
    for i in range(len(list_of_rooms)):
        for j in range(len(list_of_rooms[i])):
            if i == 0:
                link_top_row(list_of_rooms, i, j)
            elif i < hei-1:
                link_mid_rows(list_of_rooms, i, j)
            else:
                link_bottom_rows(list_of_rooms, i, j)
    return list_of_rooms[hei-1][0]

class Room:
    def __init__(self, room_name):
        self._name = room_name
        self.n = None
        self.e = None
        self.s = None
        self.w = None

    def get_name(self):
        return self._name

    def set_name(self, name):
        assert type(name) == str
        self._name = name

    def collapse_room(self):
        north = self.n
        east = self.e
        south = self.s
        west = self.w
        self.n = None
        self.e = None
        self.s = None
        self.w = None
        north.s = None
        east.w = None
        south.n = None
        west.e = None