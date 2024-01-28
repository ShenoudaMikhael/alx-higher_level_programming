#!/usr/bin/python3
"""
add integer module
"param b default is 98"
e.g:
>>> add_integer(100, 40)
140
>>> add_integer(100)
198
"""


def add_integer(a, b=98):
    """
    function to add two integers
    :param a: first integer
    :type a: int
    :param b: second integer (default is 98)
    :type b: int
    :return: the sum of a and b
    :rtype: int

    e.g:
        >>> add_integer(100, 40)
        140
        >>> add_integer(100)
        198
    """
    if not (isinstance(a, float) or isinstance(a, int)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, float) or isinstance(b, int)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
