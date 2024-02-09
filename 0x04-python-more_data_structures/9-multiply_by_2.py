#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    for value in b_dictionary:
        b_dictionary[value] = b_dictionary[value] * 2
    return b_dictionary
