#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
    If the list is empty, the function returns None
    Args:
        list (list): A list of integers.
        Defaults to an empty list if not provided
    Returns:
        int or None: The maximum value
        found in the list or None if the list is empty
    Raises:
        TypeError: If any element in the list is not an integer
    Examples:
        >>> max_integer([10, 20, -5, 7])
        20
        >>> max_integer([-10, -20, -5, -7])
        -5
        >>> max_integer()
        None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
