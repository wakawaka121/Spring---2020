"""
File: proj05_short.py
Author: Derek Tominaga
Purpose: This program contains functions that
perform actions on a linked-list but changing the
refrence to the "next" node
Course: CSC 120, spring 2020
"""

from list_node import *

def reverse_list(old_head):
    """
    This function takes one parameter to reverse the

    linked list, and print that linked list as it changes
    old_head: is a linked list of unknown length.
    returns pre_head: a linked list reversed based on
    old_head
    """
    #saves previous node while iterating through linked list
    new_head = None
    print("--- BEFORE THE LOOP ---")
    print(f"original list: {old_head}\n")
    #while head pointer exists
    while old_head is not None:
        #sets current position to start of link list
        curr = old_head
        #moves assignmnet start of old_head to next node
            #in link list
        old_head = old_head.next
        #assignts the next node of current position to
            #previous node
        curr.next = new_head
        #set previous head to current positon before
            #going to another pass of the loop
        new_head = curr
        print(f"old: {old_head}")
        print(f"new: {new_head}\n")
    return new_head

def accordion(old_head):
    """
    This fucntion takes one parameter to
    remove ever other node from a linked list
    retrun a Node that contains the meta of the
    modified linked list
    """
    #if old_head is empty or only contains 1 "element/node"
    if old_head is None or old_head.next is None:
        return None
    curr = old_head.next
    while curr is not None and curr.next is not None:
        #changes curr points to two nodes over
        curr.next = curr.next.next
        #moves cur to pointer
        curr = curr.next
    return old_head.next

def insert_at(old_head, new_head, pos):
    """
    This program takes three parameters to insert
    a new node at a particular position.
    old_head: is a linked list
    new_head: is a node with a value but no pointer
    pos: is an int value to indicate where to insert
    """
    assert pos >= 0
    curr = old_head
    #number of elemetes in the linked list
    num_of_nodes = 0
    #counter to keep track of position
    count = 0
    #will traverse through the linked list
        # to determine number of elements
    while curr is not None:
        num_of_nodes += 1
        curr = curr.next
    curr = old_head
    #if old_head is an empty linked list
    if old_head is None:
        assert pos is 0
        old_head = new_head
        return old_head
    assert pos <= num_of_nodes
    while count < num_of_nodes:
        count +=1
        if pos is 0:
            new_head.next = old_head
            old_head = new_head
            return old_head
        #this will insert at a specific position
        if pos == count:
            new_head.next = curr.next
            curr.next = new_head
            curr = new_head
            return old_head
        curr = curr.next
    return old_head

def too_many_aliases():
    """
    This function makes a list that contains
    refrences to lists that contains refrences to
    list.
    returns a list with the refrences
    """
    list_1 = [11,22]
    list_2 = [33,44]
    list_3 = [list_1, list_2]
    list_4 = [list_1, list_2]
    list_5 = [list_3,list_4,list_3,list_4]
    return list_5