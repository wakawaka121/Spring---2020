#! /usr/bin/python3

""" Code to test the accordion() function

    Authors: Russ Lewis   (based, very vaguely, on older code by Saumya Debray)
"""

import list_node
import proj05_short



def main():
    print("Testing insert_at()...")
    print()

    values    = ["the_one_and_only"]
    positions = [ 0 ]
    nodes     = [list_node.ListNode(val) for val in values]

    assert len(positions) == len(values)
    assert len(  nodes  ) == len(values)


    data = None
    print(f"Original list: {data}")


    for i in range(len(values)):
        print(f"Inserting a node with the value {values[i]}, at position {positions[i]}")
        data = proj05_short.insert_at(data, nodes[i], positions[i])
        print(f"List after insertion: {data}")
        print()

    expected_order = [ nodes[0] ]

    cur = data
    i   = 0
    while cur is not None:
        if cur is not expected_order[i]:
            print(f"ERROR: Node {i} in the list is not the correct node.")
        cur  = cur.next
        i   += 1


    print()
    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()

