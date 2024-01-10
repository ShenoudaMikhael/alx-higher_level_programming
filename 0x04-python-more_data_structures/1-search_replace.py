#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if len(my_list):
        new_list = list(my_list).copy()
        idx = list(my_list).index(search)
        if idx:
            new_list[idx] = replace
        return new_list
