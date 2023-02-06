"""
File: utils.py
Author: Derek Tominaga
Purpose: This file contains one function and returns the
music infromation within.
Course: CSC 120, spring 2020
"""

def read_file(file_data):
    """
    This function takes one parameter and will read through
    the "lines of a file" to make a list of tuples.
    the tuples will have 3 elements (id, song name, notes)
    file_data: an opened file object
    music_list: a list of tuples that gets returned
    """
    music_list = []
    song_tuple = []
    for lines in file_data:
        line_info = lines.strip("\n")
        #checks for empty line
        if line_info != "":
            line_info = line_info.split(" ")
            #checks if line is song info, denoted by "@" as start
            ##of line
            if line_info[0] == "@":
                song_name = ""
                #appens id to list
                song_tuple.append(int(line_info[1]))
                for cell in line_info[2:]:
                    song_name += " " + cell
                #appends song name to list
                song_tuple.append(song_name.strip())
            else:
                note_list = []
                #interates to make list of notes
                for index in range(len(line_info)):
                    note_list.append(line_info[index])
                #appends list of notes to list
                song_tuple.append(note_list)
                #appends list of (id, song mame, list of notes) as a tuple
                ##to list of songs
                music_list.append(tuple(song_tuple))
                song_tuple = []
    return music_list
def get_slices(data, slice_size):
    """
    This function takes two parameters to generate a list of
    slices of a desired length.
    data: is a slice data type
    slice_size: is an int value, that determines size of slice
    slice_list: a list of slices that gets retruned
    """
    slice_list = []
    for i in range(len(data)):
        if len(data[i:]) >= slice_size:
            slice_list.append(data[i:slice_size+i])
    return slice_list
def compare_sets(data_a, data_b):
    """
    This function takes two parameters and makes a jaccard comparison
    to get the similarity ratio between the two data structures.
    data_a: data type that gets converted to a set
    data_b: data type that gets converted to a set
    jaccard_index: is a float value that get retruned
    """
    #calculation used to get the similarity ratio between the two data sets
    jaccard_index = len(data_a & data_b)/len(data_a | data_b)
    return jaccard_index
def compare_melodies(data_a, data_b, N):
    """
    This function takes three parameter to computer the
    similarty between two songs.Will call get_slices() fucntion to
    get list of slices, and get compare_sets()
    to get similarity between the two.
    data_a: is a list of notes of the melody
    data_b: is a list of notes of the melody
    N: is an int for the size of the slice.
    similarity: is a float value that is returned
    """
    slices_of_a = get_slices(data_a, N)
    slices_of_b = get_slices(data_b, N)
    set_a = list_of_list_to_set(slices_of_a)
    set_b = list_of_list_to_set(slices_of_b)
    similarity = compare_sets(set_a, set_b)
    return similarity
def list_of_list_to_set(list_of_lists):
    """
    This funtion takes one parameter to convert
    a list of list to a set
    list_of_lists: is a list of list
    converted_set: is retruned, it is a set
    """
    converted_set = set()
    for i in range(len(list_of_lists)):
        temp_tuple = []
        for j in range(len(list_of_lists[i])):
            temp_tuple.append(list_of_lists[i][j])
        converted_set.add(tuple(temp_tuple))
    return converted_set