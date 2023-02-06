#! /usr/bin/python3

""" Code to test the accordion() function

    Authors: Russ Lewis   (based, very vaguely, on older code by Saumya Debray)
"""

import list_node
import proj05_short



def test_one(data, val, pos):
    new_node = list_node.ListNode(val)

    try:
        print(f"Starting list: {data}")
        print(f"Inserting value: {val}")
        print(f"Position: {pos}")
        print("Attempting the call, this should assert...")
        data = proj05_short.insert_at(data, new_node, pos)
        print("ERROR: The call completed normally")
    except AssertionError:
        print("OK")
    except:
        print("ERROR: The call terminated, but not because of a failed assertion.")
    print()



def main():
    print("Testing that the assertions work in insert_at()...")
    print()

    test_one(None, 123, 1)

    list1      = list_node.ListNode(456)
    list1.next = list_node.ListNode(789)
    test_one(list1, "abc", 3)

    print("TESTCASE COMPLETED")



if __name__ == "__main__":
    main()


