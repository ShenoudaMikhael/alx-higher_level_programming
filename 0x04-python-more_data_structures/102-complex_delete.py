#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = {}
    for k, v in a_dictionary.items():
        if v != value:
            new_dict[k] = v
    if len(a_dictionary) == len(new_dict):
        return a_dictionary

    a_dictionary = new_dict
    return a_dictionary
