#! /usr/bin/python3

""" Code to test the is_sorted() function

    Authors: Russ Lewis   (based, very vaguely, on older code by Saumya Debray)
"""

import list_node
import proj05_long





# INPUT:
#   First, we build a list of nodes.
#   Then we chain them together.

vals  = [('nbj', 18), ('nsn', 39), ('swc', 11), ('qkh', 24), ('ytj', 22)]
nodes = [list_node.ListNode(val) for val in vals]

in_list = nodes[0]
for i in range(len(vals)-1):
    nodes[i].next = nodes[i+1]



###########################################################
#                    TEST CODE                            #
###########################################################
def main():
    print("Testing is_sorted()...")
    print()
    print(f"Input list: {in_list}")

    retval = proj05_long.is_sorted(in_list)

    print(f"retval: {retval}")
    print()

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


