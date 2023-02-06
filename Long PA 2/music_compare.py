"""
File: music_compare.py
Author: Derek Tominaga
Purpose: This file contains two fucntions
build_map() will read in a file and parse through the
lines in the file and add them to a build_map dictionary
is_valid_map() check to make sure a map is valid.
Course: CSC 120, spring 2020
"""

import utils

def print_song_list(music_list):
    """
    This function takes one parameter to print out the list of songs
    from the file. It will list the id, song name, and notes of the song
    music_list: is a list of tuples
    """
    print ("--- SONG LIST ---")
    for index in range(len(music_list)):
        print("id=" + str(music_list[index][0]), "info=" + '"'
        + music_list[index][1] + '"' , "notes=" + str(music_list[index][2]))
def print_comparison(music_list, note_slice):
    """
    This function takes two parameters to print the comparison data
    it will iterate through the music_list to compare the similarities
    between pairs of songs and print the similarities.
    music_list: is a list of song with id and notes
    note_slice: is an int value that denotes the size of the slices to be
    compared.
    id_jaccard_dict: is a dictionary that gets returned, contains similarities
    as keys and two ids in a list as values.
    """
    id_jaccard_dict = {}
    print("\n--- COMPARISONS ---")
    index1 = 0
    while index1 < len(music_list):
        #song1 data one to be compared
        id_a = music_list[index1][0]
        melody_a = music_list[index1][2]
        index2 = (index1 + 1)
        if index2 < len(music_list):
            while index2  < len(music_list):
                #list to contain song id pairs
                id_pairs = []
                id_pairs.append(id_a)
                #song2 data to be compared
                id_b = music_list[index2][0]
                melody_b = music_list[index2][2]
                id_pairs.append(id_b)
                #get similarities betweeen two songs
                similarity = utils.compare_melodies(melody_a, melody_b,
                    note_slice)
                #add key to dict or replace existing key with
                ##new song value pair
                id_jaccard_dict[similarity] = id_pairs
                print("id_a=" + str(id_a), "id_b=" + str(id_b),
                    "similarity=" + str(similarity))
                index2 += 1
        index1 += 1
    return id_jaccard_dict
def print_results(music_list, song_similarity_dict, note_slice):
    """
    This function takes three parameters to calculate,
    format and print the results.

    music_list: is a list of tuples
    song_similarity_dict: is a dictionary with keys are
    similarities and values as list of ids.
    note_slice: is a int value denoting size of slice
    """
    #gets song most similar
    most_similar =max(song_similarity_dict)
    #gets list of song pair for most similar
    song_pair = song_similarity_dict[most_similar]
    #loops through song pair to get ids and notes
    for i in range(len(music_list)):
        if song_pair[0] in music_list[i]:
            song_1 = music_list[i][1]
            tuple_1 = music_list[i][2]
        if song_pair[1] in music_list[i]:
            song_2 = music_list[i][1]
            tuple_2 = music_list[i][2]
    #converts two melodies to strings to print in desired format
    melody_1, melody_2 = tuple_to_string(tuple_1, tuple_2)
    print("\n--- RESULT ---")
    print("Most similar songs:")
    print("  " + song_1 + "\n" + "  "+  song_2 + "\n")
    print("  ids:", str(song_pair[0]))
    print ("  ids:", str(song_pair[1]))
    print("\nMelodies:")
    print("    " + melody_1 + "\n" + "    " + melody_2 + "\n")
    print("Set 1")
    #called to print slices as strings
    set_as_string(tuple_1, note_slice)
    print("\nSet 2")
    #same as above for set 1
    set_as_string(tuple_2, note_slice)
def set_as_string(tuple_list, note_slice):
    """
    This function takes two parameters to convert list of
    slices into string for printing in output format.
    By calling the get slices function. Then prints
    each slice as a string
    tuple_list: is a list of notes that gets sliced
    note_slice: int value that denotes size of slice.
    """
    slice_list = utils.get_slices(tuple_list, note_slice)
    slice_set = set()
    for i in range(len(slice_list)):
        temp_tuple = []
        for j in range(len(slice_list[i])):
            temp_tuple.append(slice_list[i][j])
        slice_set.add(tuple(temp_tuple))
    for i in sorted(slice_set):
        slice_string = ""
        for j in i:
            slice_string += j + " "
        slice_string = slice_string.strip()
        print("  " + slice_string)
def tuple_to_string(tuple_1, tuple_2):
    """
    This function takes two parameters to and convertes the tuple into
    a string.
    tuple_1: is a tuple of notes from a song
    tuple_2: is a tuple of notes from a song
    returns two strings for the melodies of the songs
    """
    melody_string_1 = ""
    melody_string_2 = ""
    for i in tuple_1:
        melody_string_1 += i + " "
    for j in tuple_2:
        melody_string_2 += j + " "
    return melody_string_1, melody_string_2
def main():
    input_string = input("file:")
    note_slice = int(input("n:"))
    file_data = open(input_string, "r")
    music_list = utils.read_file(file_data)
    print_song_list(music_list)
    song_similarity_dict = print_comparison(music_list, note_slice)
    print_results(music_list, song_similarity_dict, note_slice)

if __name__ == "__main__":
    main()