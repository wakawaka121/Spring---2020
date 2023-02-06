from list_node import *

def reverse_list(old_head):
    cur = old_head
    new_head = None
    if cur is None:
        return cur
    while cur is not None:
        next_node = cur.next
        cur.next = new_head
        new_head = cur
        cur = next_node
    return new_head

        #if cur.next.next is None:
        #    new_head = cur.next
        #    cur.next = None
        #while cur.next is not None:
        #    new_head.next =
