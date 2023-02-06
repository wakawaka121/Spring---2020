#!/usr/bin/env python3


""" Code to test the maze.py program"""

import maze



# ------- CONFIG VALUES ------
# (Change these to alter what the testcase does)

edges = [ ['a','b'], ['a','c'], ['b','c'], ['b','d'], ['a','e'], ['e','d'], ['b','e'] ]
src = 'a'
dst = 'd'

sols = [ ['a','b','d'], ['a','b','e','d'], ['a','c','b','d'], ['a','c','b','e','d'], ['a','e','b','d'], ['a','e','d'] ]



# ------- TESTCASE BODY --------
print("PROBLEM DEFINITION:")
print(f"  edges: {edges}")
print(f"  src:   {src}")
print(f"  dst:   {dst}")
print("ACCEPTABLE SOLUTIONS:")
for sol in sols:
    print(f"  {sol}")
print()

print("Creating the Maze object...")
the_maze = maze.Maze(edges)
print()

print(f"Calling solve({src},{dst})...")
my_sol = the_maze.solve(src,dst)
print()

print("NOTE: I am *not* printing the solution, because I want the output to be the same, no matter which of the solutions a given student returns.")
print()

if my_sol in sols:
    print("OK!  The returned solution was in the set of expected solutions.")
else:
    print("ERROR: The returned solution was not a correct solution.")
print()

print("TESTCASE COMPLETED")

