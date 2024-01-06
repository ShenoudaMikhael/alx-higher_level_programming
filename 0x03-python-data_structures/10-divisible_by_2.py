#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Return a new list with True or False, depending on whether
    the integer at the same position in the original list is a multiple of 2
    The new list should have the same size as the original list"""
    return [my_list[i] % 2 == 0 for i in range(len(my_list))]
