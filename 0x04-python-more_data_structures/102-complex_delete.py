#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k in a_dictionary.copy():
        if a_dictionary[k] == value:
            a_dictionary.pop(k)
    return a_dictionary
