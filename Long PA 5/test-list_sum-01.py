#! /usr/bin/python3

""" Code to test the list_sum() function

    Authors: Russ Lewis   (based, very vaguely, on older code by Saumya Debray)
"""

import list_node
import proj05_long





# INPUT:
#   First, we build a list of nodes.
#   Then we chain them together.

vals  = [-38]
nodes = [list_node.ListNode(val) for val in vals]

in_list = nodes[0]
for i in range(len(vals)-1):
    nodes[i].next = nodes[i+1]



###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    print("Testing list_sum()...")
    print()
    print(f"Input list: {in_list}")

    retval = proj05_long.list_sum(in_list)

    print(f"retval: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


