#! /usr/bin/python3


from list_of_rows_0_on_bottom import *



def test_one(w,h, update_list):
    print("--- test_one() : BEGINNING TEST ---")
    print(f"  w = {w}")
    print(f"  h = {h}")
    print(f"  update_list = {update_list}")
    print()

    print("Calling build_rect(w,h)")
    a = build_rect(w,h)
    print(f"  returned: {a}")
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
    print(f"  {a}")
    print()

    print("--- print_rect() START ---")
    print_rect(a)
    print("--- print_rect() END ---")
    print()

    return a



test_one(20,8, [(2,2), (3,3)])


print()
print("TESTCASE COMPLETED")
