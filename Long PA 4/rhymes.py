"""
File: rhymes.py
Author: Derek Tominaga
Purpose: This program reads a file to create
key:value dictionaries for words and
there phoneme pronunciation. It will then list
takes 3 words and list the words that match
the "perfect rhyme" difiniton from wikipedia.
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

def make_phonemes_dict(file_name):
    """
    This function takes one paremeter to open a
    text file that contains a word and its phonemes.
    This builds a dictionary of key: words and
    value: phoneme of word.
    file_name: is a string that is name of text file
    return phonemes_dict and reversed_phonemes
    """
    phonemes_dict = {}
    reversed_phonemes = {}
    dict_lines_data = open(file_name, "r")
    for lines in dict_lines_data:
        line_info = lines.strip("\n").split()
        key_word = line_info[0]
        line_info.pop(0)
        #makes key:value (word:phoneme) entry
        if key_word not in phonemes_dict:
            phonemes_dict[key_word] = set()
            phonemes_dict[key_word].add(tuple(line_info))
        else:
        #if key word has two pronunciations add to set of phonemes
            phonemes_dict[key_word].add(tuple(line_info))
        if tuple(line_info) not in reversed_phonemes:
        #make key:value (phoneme:word) entry
            reversed_phonemes[tuple(line_info)] = set()
            reversed_phonemes[tuple(line_info)].add(key_word)
        else:
        #if phoneme has more than one word representation add to
        ## set of words
            reversed_phonemes[tuple(line_info)].add(key_word)
    return phonemes_dict, reversed_phonemes
def look_up_phoneme_stress(word, phonemes_dict):
    """
    This function takes two parameters to find the
    stressed sound and the phoneme preceding the stressed
    sound.
    word: is a string , that is the word being searched
    phonemes_dict: is a dictionary, keys: words and
        values: are the pronunciation phoneme.
    returns phoneme_to_match: a list of tuple(s)
    and preceding_sound: a string.
    """
    phoneme_to_matchs = []
    phonemes = phonemes_dict[word]
    preceding_sound = ""
    for i in phonemes:
        for j in range(len(i)):
            if i[j][-1] == "1":
                stress_location = j
                if (j-1) >= 0:
                    preceding_sound = i[j-1]
                phoneme_to_matchs.append(i[stress_location:])
    return phoneme_to_matchs, preceding_sound

def find_rhymes(phoneme_to_match, preceding_sound, reversed_phonemes):
    """
    This function takes three parameters to make a set of words
    that rhyme.
    phoneme_to_match: list of strings that needs to be matched
    preceding_sound: is a string that gets compared
    reversed_phonemes: is a dictionay, key: phoneme
    and values: set of words that have that phoneme
    return rhyming_words as a set of strings.
    """
    rhyming_words = set()
    for phoneme in phoneme_to_match:
        #determines number of matches needed to be ryhme
        elements_to_match = len(phoneme)
        for key in reversed_phonemes.keys():
            #number of matches found between data
            match_between_data = compare_back(phoneme, key)
            #if words total phoneme is whole pronunciation of word
            ## doesnt count as rhyme canidate
            if len(key) == elements_to_match:
                continue
            elif elements_to_match == match_between_data:
                if len(preceding_sound) == 0:
                    return rhyming_words
                #make sure sound before stressed sound is not same
                if key[:-elements_to_match][-1] != preceding_sound:
                    for words in reversed_phonemes[key]:
                        rhyming_words.add(words)
    return rhyming_words

def print_word_rhymes(word, list_of_rhymes):
    """
    This function take two parameters to print
    the word and its rhyming matches.
    word: is a string in all caps, the words to
    make a rhyme with.
    list_of_rhymes: is a set of strings, of the words
    that rhyme with "word" parameter
    """
    print("Rhymes for:", word)
    if len(list_of_rhymes) == 0:
        print("  -- none found --")
    else:
        for i in sorted(list_of_rhymes):
            print ("  " + i)

def main():
    file_name = input()
    phonemes_dict, reversed_phonemes = make_phonemes_dict(file_name)
    word_one = input().upper()
    word_two = input().upper()
    word_three = input().upper()
    phoneme_to_match, preceding_sound = look_up_phoneme_stress(word_one,
        phonemes_dict)
    word_one_rhymes = find_rhymes(phoneme_to_match, preceding_sound,
        reversed_phonemes)
    print_word_rhymes(word_one, word_one_rhymes)
    print()
    phoneme_to_match, preceding_sound = look_up_phoneme_stress(word_two,
        phonemes_dict)
    word_two_rhymes = find_rhymes(phoneme_to_match, preceding_sound,
        reversed_phonemes)
    print_word_rhymes(word_two, word_two_rhymes)
    print()
    phoneme_to_match, preceding_sound = look_up_phoneme_stress(word_three,
        phonemes_dict)
    word_three_rhymes = find_rhymes(phoneme_to_match, preceding_sound,
        reversed_phonemes)
    print_word_rhymes(word_three, word_three_rhymes)

if __name__ == "__main__":
    main()