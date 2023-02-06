#! /usr/bin/python3


from dictionary_grid import *



def test_one(w,h, update_list):
    print("--- test_one() : BEGINNING TEST ---")
    print(f"  w = {w}")
    print(f"  h = {h}")
    print(f"  update_list = {update_list}")
    print()

    print("Calling build_rect(w,h)")
    a = build_rect(w,h)
    print(f"  returned: {reinsert_by_key_order(a)}")
    print()

    print("--- print_rect() START ---")
    print_rect(a)
    print("--- print_rect() END ---")
    print()

    print("Editing the rectangle...")
    for (x,y) in update_list:
        print(f"  Changing ({x},{y})")
        update(a, x,y, 'x')
    print()

    print("Raw data structure after the change:")
    print(f"  {reinsert_by_key_order(a)}")
    print()

    print("--- print_rect() START ---")
    print_rect(a)
    print("--- print_rect() END ---")
    print()

    return a



def reinsert_by_key_order(orig):
    retval = {}
    for k in sorted(orig.keys()):
        retval[k] = orig[k]
    return retval



test_one(5,5, [(1,1), (2,1), (3,1), (3,3)])


print()
print("TESTCASE COMPLETED")

