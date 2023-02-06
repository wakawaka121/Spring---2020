"""
File: cover_list_code.py
Author: Derek Tominaga
Purpose: This program contains test-cases
that will go through all ines in list_insert.py
Course: CSC 120, spring 2020
"""

from list_insert import *

def main():
    #objects for pass 1
    obj1 = ListNode( (1,2) )
    obj2 = ListNode( (3,4) )
    #objects for pass 2
    obj3 = ListNode( (1,4) )
    obj4 = ListNode( (3,3) )
    #objects for pass 3
    obj5 = ListNode( (4,4,) )
    obj6 = ListNode( (3,4) )
    #objects for pass 4
    obj7 = ListNode( (1,2) )
    obj8 = ListNode( (3,1) )
    obj9 = ListNode ( (1,2) )
    #objects for pass 5
    obj10 = ListNode( (1,2) )
    obj11 = ListNode( (5,6) )
    obj12 = ListNode( (3,4) )
    #objects for pass 6
    obj13 = ListNode( (5,6) )
    obj14 = ListNode( (7,8) )
    obj15 = ListNode( (9,10) )
    #pass 1
    data = sorted_list_insert(None, obj1)
    data = sorted_list_insert(data, obj2)
    data = sorted_list_insert(None, None)
    print_list(data)
    #pass 2
    data = sorted_list_insert(None, obj3)
    data = sorted_list_insert(data, obj4)
    print_list(data)
    #pass 3
    #initilizes as empty
    data = sorted_list_insert(None, None)
    data = sorted_list_insert(None, obj5)
    data = sorted_list_insert(data, obj6)
    print_list(data)
    #pass 4
    data = sorted_list_insert(None, None)
    data = sorted_list_insert(None, obj7)
    data = sorted_list_insert(data, obj8)
    data = sorted_list_insert (data, obj9)
    #pass 5
    data = sorted_list_insert(None, None)
    data = sorted_list_insert(None, obj10)
    data = sorted_list_insert(data, obj11)
    data = sorted_list_insert(data, obj12)
    #pass 6
    data = sorted_list_insert(None,None)
    data = sorted_list_insert(None, obj13)
    data = sorted_list_insert(data, obj14)
    data = sorted_list_insert(data, obj15)


if __name__ == "__main__":
    main()