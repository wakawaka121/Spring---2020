"""
File: proj05_long.py
Author: Derek Tominaga
Purpose: This program contains functions
related to linked list. Each function
works with a linked list to perfrom
a particular action on the linked list.
Course: CSC 120, spring 2020
"""

from list_node import *

def is_sorted(head):
    """
    This function takes one paramenter that will
    check if linked list is sorted in ascending
    order.
    head: is a linked list refrence
    returns True if it is sorted, false is not.
    """
    curr = head
    while curr is not None and curr.next is not None:
        if curr.val > curr.next.val:
            return False
        curr = curr.next
    return True

def list_sum(head):
    """
    This function takes one parameter and will
    add up all the values from the linked list.
    head: is a
    """
    sum_of_ll = 0
    if head is None:
        return sum_of_ll
    curr = head
    while curr is not None:
        sum_of_ll += curr.val
        curr = curr.next
    return sum_of_ll

def pair(list1, list2):
    """
    This function takes two parameters to pair
    the contents of each will be added as a tuple
    in a another lnked list.
    list1:
    """
    head1 = list1
    head2 = list2
    pair_ll = None
    while head1 is not None and head2 is not None:
        if pair_ll is None:
            pair_ll = ListNode( (head1.val, head2.val) )
            head1 = head1.next
            head2 = head2.next
            curr = pair_ll
        new_node = ListNode( (head1.val, head2.val) )
        curr.next = new_node
        head1 = head1.next
        head2 = head2.next
        curr = curr.next
    return pair_ll

def return_new_node(head1, head2):
    """
    This function takes two parameters to
    create a new node, and move the the
    the pointer of the linked list
    head1: is a linked list refrence
    head2: is a linked lost refrence
    return: new_node which a link list node;
    head1 and head2 as they "move"
    """
    if head1 is None:
        new_node = ListNode( (None, head2.val) )
        head2 = head2.next
    elif head2 is None:
        new_node = ListNode ( (head1.val, None) )
        head1 = head1.next
    else:
        new_node = ListNode( (head1.val, head2.val) )
        head1 = head1.next
        head2 = head2.next
    return new_node, head1, head2


def print_pair_partial(list1, list2):
    """
    This funtion takes two parameters and will print
    values of the two list paired with eachother
    list1: is a linked list of unknown length
    list2: is a linked list of unknown length
    """
    head1 = list1
    head2 = list2
    pair_ll = None
    if pair_ll is None:
        new_node, head1, head2 = return_new_node(head1, head2)
        print(f"1: {new_node.val[0]}", f"2: {new_node.val[1]}")
    while head1 is not None or head2 is not None:
        new_node, head1, head2 = return_new_node(head1, head2)
        print(f"1: {new_node.val[0]}", f"2: {new_node.val[1]}")

def pair_partial(list1, list2):
    """
    This function takes two parameters to pair values of
    list1 with values of list2. This pair is added as
    a tuple value into a linked list.
    list1: linked list of unknow number of nodes
    list2: linked list of unknown number of nodes
    pair_ll: is a linked list with tuple pairs as values,
    pair_ll is returned
    """
    head1 = list1
    head2 = list2
    pair_ll = None
    if pair_ll is None:
        pair_ll, head1, head2 = return_new_node(head1, head2)
    curr = pair_ll
    while head1 is not None or head2 is not None:
        new_node, head1, head2 = return_new_node(head1, head2)
        curr.next = new_node
        curr = curr.next
    return pair_ll