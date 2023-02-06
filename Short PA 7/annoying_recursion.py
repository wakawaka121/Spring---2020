"""
File: annoying_recursion.py
Author: Derek Tominaga
Purpose: This program contains functions
that perform math identities  in an recursive
fashion.
Course: CSC 120, spring 2020
"""

def annoying_factorial(n):
    """
    This function takes one parameter to
    perform factorial in a recursive fashion.
    fulfilling the "annoying" criteria.
    n: is an int value
    return: int value that is n!
    """
    assert n >= 0
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 6
    elif n == 4:
        return 4 * annoying_factorial(3)
    elif n == 5:
        return 5 * annoying_factorial(4)
    elif n == 6:
        return 6 * annoying_factorial(5)
    else:
        return n * annoying_factorial(n-1)

def annoying_fibonacci(n):
    """
    This function takes one parameter to
    perform a fibonacci sequence in a
    resursive fashion. fulfilling the
    "annoying" criteria.
    n: is an int value
    return: int value that is f(n)
    """
    assert n >= 0
    if n == 0:
        return 0
    elif n== 1:
        return 1
    elif n == 2:
        return 1
    elif n== 3:
        return 2
    elif n== 4:
        return annoying_fibonacci(3) + 1
    elif n== 5:
        return annoying_fibonacci(4) + 2
    elif n == 6:
        return annoying_fibonacci(5) + 3
    else:
        return annoying_fibonacci(n-1) + annoying_fibonacci(n-2)

def annoying_valley(n):
    """
    This function takes one parameter and
    will print a valley whose "depth" is
    determined by the parameter.
    fulfills the "annoying" criteria.
    n: is an int value
    """
    assert n >= 0
    if n == 0:
        print()
    elif n == 1:
        print("*")
    elif n == 2:
        print("./")
        print("*")
        print(".\\")
    elif n == 3:
        print("../")
        print("./")
        print("*")
        print(".\\")
        print("..\\")
    elif n == 4:
        print(".../")
        annoying_valley(3)
        print("...\\")
    elif n == 5:
        print("..../")
        annoying_valley(4)
        print("....\\")
    elif n == 6:
        print("...../")
        annoying_valley(5)
        print(".....\\")
    else:
        print(("." * (n-1)) + "/" )
        annoying_valley(n-1)
        print(("." * (n-1)) + "\\" )

def annoying_int_sequence(n):
    """
    This function takes one parameter to
    return sequence based off the parameter.
    n: is an int value
    return: a list, that contains the sequence
    """
    assert n >= 0
    if n == 0:
        sequence_list = []
        return sequence_list
    elif n == 1:
        sequence_list = [1]
        return sequence_list
    elif n == 2:
        sequence_list = [1,2,1]
        return sequence_list
    elif n == 3:
        sequence_list = [1,2,1,3,1,2,1,3,1,2,1]
        return sequence_list
    elif n == 4:
        insert = annoying_int_sequence(3)
        insert_with_n = annoying_int_sequence(3)
        insert_with_n.append(4)
        return (insert_with_n *3) + insert
    elif n == 5:
        insert = annoying_int_sequence(4)
        insert_with_n = annoying_int_sequence(4)
        insert_with_n.append(5)
        return (insert_with_n *4) + insert
    elif n == 6:
        insert = annoying_int_sequence(5)
        insert_with_n = annoying_int_sequence(5)
        insert_with_n.append(6)
        return (insert_with_n *5) + insert
    else:
        insert = annoying_int_sequence(n-1)
        insert_with_n = annoying_int_sequence(n-1)
        insert_with_n.append(n)
        return (insert_with_n *(n-1)) + insert