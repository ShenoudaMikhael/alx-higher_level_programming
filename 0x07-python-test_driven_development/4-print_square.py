#!/usr/bin/python3
"""
print square module
"""


def print_square(size):
    """
    Function to print a square of * characters.
    Args:
    size (int): The number of rows or columns in the square.
    Returns:
    None

    """

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if not size >= 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for __ in range(size):
            print("#", end="")
        print("")
