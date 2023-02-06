"""
File: shapes.py
Author: Derek Tominaga
Purpose: This program contains functions that
make the refrence diagrams of the images from
spec.
Course: CSC 120, spring 2020
"""
def shape_alpha():
    """
    This funtion takes no parameters, makes
    a list with elements that are list.
    returns a list of list of refrences
    """
    index_0_of_list_2 = [1.1, -17]
    index_1_of_list_2 = [123, 456]
    value_1 = 10
    value_2 = 40
    var1 = "abc"
    var2 = "jkl"
    list_0 = [value_1, var1, var2, value_2]
    list_1 = [index_0_of_list_2, index_1_of_list_2]
    primary_list = [list_0, list_1]
    return primary_list

def shape_bravo():
    """
    This function takes no argument to
    generate a list of list that contain
    refrences to another list that contain
    values
    returns the list with list of refrences
    """
    var1 = "whoa"
    var2 = "excellent"
    var3 = "bogus"
    var4 = "righteous"
    var5 = "rufus"
    header_1_next = [var3, var4]
    header_2_next = header_1_next
    values_1 = [var1,var2]
    header_1 = [values_1, header_1_next]
    header_2 = [header_2_next, var5]
    list_object = [header_1, header_2]
    return list_object

def shape_charlie(arg1):
    """
    This function takes one parameter
    this funciton makes a list of refrences
    to a list with a refrence and a value
    contained in it. Fine refrences contains
    None and a value.
    arg1: is an undetermined data type.
    retuns pointer to first list.
    """
    header_3 = [None, arg1]
    header_2 = [header_3, arg1]
    header_1 = [header_2, arg1]
    main_list = [header_1, arg1]
    return main_list

def shape_delta(arg1, arg2):
    """
    This function takes two parameters to build
    a list that containes the parameters in specific
    positions of a list, a pointer to another list,
    and a pointer to a list with a value
    arg1/arg2: are undetermined data types
    returns pointer to first list
    """
    value_1 = [10]
    value_2 = [20]
    value_3 = [30]
    header_3 = [arg1, arg2]
    header_2 = [arg1, arg2, header_3 , value_3]
    header_1 = [arg1, header_2, value_2, arg2]
    main_list = [arg1, arg2, header_1, value_1]
    return main_list

def shape_echo(arg1, arg2, arg3):
    """
    This function takes 3 parameters to build
    a list with refrences to another list
    that contain the parameters and points to
    another list, eventually pointing to
    the frist list.
    arg1/arg2/arg3: are undetermined types
    returns pointer to first list
    """
    header_1 = [None, arg1]
    header_2 = [None, arg2]
    header_3 = [None, arg3]
    header_1[0] = header_2
    header_2[0] = header_3
    header_3[0] = header_1
    return header_1