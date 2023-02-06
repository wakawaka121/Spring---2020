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
    print(f"Dumping all of the cells:")

    for x in range(pipes.get_wid()):
        for y in range(pipes.get_hei()):
            print(f"({x},{y}) : {repr(pipes.get_cell(x,y))}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


