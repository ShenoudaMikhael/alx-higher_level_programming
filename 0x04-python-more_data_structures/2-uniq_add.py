#!/usr/bin/python3


def uniq_add(my_list=[]):
    """sum all unique items in list"""
    if len(my_list) > 0:
        return sum(set(my_list))
    return 0
