#! /usr/bin/python3

""" Code to test the Pipes class

    Authors: Russ Lewis
"""

from pipegrid import Pipes



IN_GRID = [["s+",    "ns",    "nes",   "ns",    "e+"    ],
           ["nw",    "sw",    "ew",    "ne",    "sw"    ],
           ["nesw+", "nesw+", "nesw+", "nesw+", "nesw+" ],
           ["ns",    "ne",    "new+",  "nsw",   "ns"    ],
           ["s+",    "new",   "s+",    "s+",    "s+"    ]]
SIZE = 100



def main():
    print("Creating a Pipes class (basic test)")
    print("-----------------")
    print()
    print(f"Input list: {IN_GRID}")
    print()

    pipes = Pipes(IN_GRID, SIZE)

    print("-----------------")
    print(f"Reading the cell at (1,4) : {repr(pipes.get_cell(1,4))}")
    print(f"Reading the cell at (4,1) : {repr(pipes.get_cell(4,1))}")
    print()

    print("Rotating (1,4) once...")
    pipes.rotate_ccw(1,4)
    print(f"Reading the cell at (1,4) : {repr(pipes.get_cell(1,4))}")
    print(f"Reading the cell at (4,1) : {repr(pipes.get_cell(4,1))}")
    print()

    print("Setting the fill state at (1,4) to True...")
    pipes.set_fill_state(1,4, True)
    print(f"Reading the cell at (1,4) : {repr(pipes.get_cell(1,4))}")
    print(f"Reading the cell at (4,1) : {repr(pipes.get_cell(4,1))}")
    print()

    print("Rotating (1,4) once...")
    pipes.rotate_ccw(1,4)
    print(f"Reading the cell at (1,4) : {repr(pipes.get_cell(1,4))}")
    print(f"Reading the cell at (4,1) : {repr(pipes.get_cell(4,1))}")
    print()

    print("Rotating (1,4) once...")
    pipes.rotate_ccw(1,4)
    print(f"Reading the cell at (1,4) : {repr(pipes.get_cell(1,4))}")
    print(f"Reading the cell at (4,1) : {repr(pipes.get_cell(4,1))}")
    print()

    print("Rotating (1,4) once...")
    pipes.rotate_ccw(1,4)
    print(f"Reading the cell at (1,4) : {repr(pipes.get_cell(1,4))}")
    print(f"Reading the cell at (4,1) : {repr(pipes.get_cell(4,1))}")
    print()

    print("Rotating (1,4) once...")
    pipes.rotate_ccw(1,4)
    print(f"Reading the cell at (1,4) : {repr(pipes.get_cell(1,4))}")
    print(f"Reading the cell at (4,1) : {repr(pipes.get_cell(4,1))}")
    print()

    print("Rotating (1,4) three times...")
    pipes.rotate_ccw(1,4)
    pipes.rotate_ccw(1,4)
    pipes.rotate_ccw(1,4)
    print(f"Reading the cell at (1,4) : {repr(pipes.get_cell(1,4))}")
    print(f"Reading the cell at (4,1) : {repr(pipes.get_cell(4,1))}")
    print()

    print("Rotating (4,1) once...")
    pipes.rotate_ccw(4,1)
    print(f"Reading the cell at (1,4) : {repr(pipes.get_cell(1,4))}")
    print(f"Reading the cell at (4,1) : {repr(pipes.get_cell(4,1))}")
    print()

    print("-----------------")
    print(f"Dumping all of the cells:")

    for x in range(pipes.get_wid()):
        for y in range(pipes.get_hei()):
            print(f"({x},{y}) : {repr(pipes.get_cell(x,y))}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()

