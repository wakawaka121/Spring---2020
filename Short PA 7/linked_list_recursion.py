"""
File: linked_list_recursion.py
Author: Derek Tominaga
Purpose: This program contains functions
that would be methods in a linked list Class.
This function perform their actions recursively.
Course: CSC 120, spring 2020
"""

from list_node import *

def is_sorted_recursive(head):
    curr = head
    if curr is None:
        return True
    if curr.next is None:
        return True
    if curr.val > curr.next.val:
        return False
    else:
        curr = curr.next
        return is_sorted_recursive(curr)

"""
falied attempt

def accordion_recursive(head):
    curr = head
    if head is None or head.next is None:
        return None
    if head.next.next is None:
        curr.next = None
    else:
        curr = curr.next
    if curr.next is not None:
        curr.next = curr.next.next
        accordion_recursive(curr.next)
    return head.next
"""


"""

failed attmept 2

def accordion_recursive(head):
    if head is None or head.next is None:
        return None
    curr = head
    curr2 = head.next
    if curr.next is not None:
        curr.next = curr.next.next
        curr2.next = curr2.next.next
        accordion_recursive(curr.next)
    return head.next

"""

"""

failed attempt 3

def accordion_recursive(head):
    curr_movement = head.next
    if head is None or head.next is None:
        return None
    curr = head
    if curr.next is not None:
        curr_movement.next = curr.next.next
        accordion_recursive(curr.next)
    return head.next

"""

def accordion_recursive(head):
    if head is None or head.next is None:
        return None
    curr = head
    curr2 = head.next
    if curr.next is not None:
        curr.next = curr.next.next
        if curr2.next is not None:
            curr2.next = curr2.next.next
    accordion_recursive(curr.next)
    return curr2

"""

test case

no1 = ListNode("a")
no2 = ListNode("b")
no3 = ListNode("c")
no4 = ListNode("d")
no5 = ListNode("e")
#no6 = ListNode("f")
no1.next = no2
no2.next = no3
no3.next = no4
no4.next = no5
no5.next = None
#no6.next = None

"""