#! /usr/bin/python3

""" Code to test the Pipes class

    Authors: Russ Lewis
"""

from pipegrid import Pipes



IN_GRID = [["w+",    "es",    "ew",    "sw",    "ne",    "s+"    ],
           ["esw",   "es",    "w+",    "new+",  "esw",   "s+"    ],
           ["w+",    "n+",    "nes",   "sw",    "sw",    "es"    ]]
SIZE = 125.2



def main():
    print("Creating a Pipes class (basic test)")
    print("-----------------")
    print()
    print(f"Input list: {IN_GRID}")
    print()

    pipes = Pipes(IN_GRID, SIZE)

    print("-----------------")
    print(f"width:  {pipes.get_wid()}")
    print(f"height: {pipes.get_hei()}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


