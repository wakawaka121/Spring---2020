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
    print(f"Reading the cell at (2,3) : {repr(pipes.get_cell(2,3))}")
    print(f"Reading the cell at (3,2) : {repr(pipes.get_cell(3,2))}")
    print()

    print("Setting the fill state at (2,3) to True...")
    pipes.set_fill_state(2,3, True)
    print(f"Reading the cell at (2,3) : {repr(pipes.get_cell(2,3))}")
    print(f"Reading the cell at (3,2) : {repr(pipes.get_cell(3,2))}")
    print()

    print("Setting the fill state at (2,3) to True (a second time, redundant)...")
    pipes.set_fill_state(2,3, True)
    print(f"Reading the cell at (2,3) : {repr(pipes.get_cell(2,3))}")
    print(f"Reading the cell at (3,2) : {repr(pipes.get_cell(3,2))}")
    print()

    print("Setting the fill state at (2,3) to False...")
    pipes.set_fill_state(2,3, False)
    print(f"Reading the cell at (2,3) : {repr(pipes.get_cell(2,3))}")
    print(f"Reading the cell at (3,2) : {repr(pipes.get_cell(3,2))}")
    print()

    print("Setting the fill states at (2,3) and (3,2) to True...")
    pipes.set_fill_state(2,3, True)
    pipes.set_fill_state(3,2, True)
    print(f"Reading the cell at (2,3) : {repr(pipes.get_cell(2,3))}")
    print(f"Reading the cell at (3,2) : {repr(pipes.get_cell(3,2))}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


