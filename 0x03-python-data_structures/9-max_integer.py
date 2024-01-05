#!/usr/bin/python3
def max_integer(my_list=[]):
    """Returns the maximum integer in a list.
    If the list is empty, returns None."""
    if len(my_list) == 0:
        return None
    max_num = my_list[0]
    for i in range(len(my_list)):
        max_num = my_list[i] if my_list[i] > max_num else max_num
    return max_num
