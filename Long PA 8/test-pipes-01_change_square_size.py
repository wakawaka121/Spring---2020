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
    print(f"square_size: {pipes.get_square_size()}")
    print()

    print("-----------------")
    print("Setting the square size to 75...")
    pipes.set_square_size(75)
    print(f"new square_size: {pipes.get_square_size()}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()

