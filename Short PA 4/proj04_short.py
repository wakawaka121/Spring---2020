"""
File: proj04_short.py
Author: Derek Tominaga
Purpose: This program contain functions
to compare linear data sets, from front
to back and back to front. And a function
that will tell where the primary stress
occurs.
Course: CSC 120, spring 2020
"""
def compare_length(data_one, data_two):
    """
    This function takes two parameters to determine
    max number of elements to check. Type of data_one
    must be same as data_two
    data_one: data structure of(str, list or tuple)
    data_two: data structure of  (str, list or tuple)
    returns 0, length_one, or length_two as int values
    """
    length_one = len(data_one)
    length_two = len(data_two)
    if length_one == 0 or length_two == 0:
        return 0
    if length_one == length_two:
        return length_two
    if length_one > length_two:
        return length_two
    if length_one < length_two:
        return length_one
def compare_front(data_one, data_two):
    """
    This functions take two parameters of any
    linear data type. it will compare the parameters
    and keep track of the number of element that
    are similar from the front (index 0)
    data_one/two: are liner data types (str, list or tuple)
    return number of times a match was found as int value
    """
    assert type(data_one) == type(data_two)
    #to get max comparisons
    max_length = compare_length(data_one,data_two)
    match_count = 0
    count = 0
    while count < max_length and data_one[count] == data_two[count]:
        match_count += 1
        count += 1
    return match_count
def compare_back(data_one, data_two):
    """
    This functions take two parameters of any
    linear data type. it will compare the parameters
    and keep track of the number of element that
    are similar from the back (index -1)
    data_one/two: are liner data types (str, list or tuple)
    return number of times a match was found as int value
    """
    assert type(data_one) == type(data_two)
    #to get max comparisons
    max_length = compare_length(data_one,data_two)
    match_count = 0
    count = 1
    while count <= max_length and data_one[-count] == data_two[-count]:
        match_count += 1
        count += 1
    return match_count
def primary_stress(set_of_phonemes):
    """
    This function takes one to identify the location
    as an index of the primary stress, denoted by 1 in
    its phoneme.
    set_of_phonemes: is a set of strings(phonemes)
    returns the index as int value, where primary
    stress occured
    """
    assert type(set_of_phonemes) == list
    assert len(set_of_phonemes) != 0
    for i in range(len(set_of_phonemes)):
        assert len(set_of_phonemes[i]) > 0

        if set_of_phonemes[i][-1] == "1":
            return i