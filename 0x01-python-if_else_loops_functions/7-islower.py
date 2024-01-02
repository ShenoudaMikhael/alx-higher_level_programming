#!/usr/bin/env python3
def islower(c):
    """
    Checks if a given character is lowercase.

    Args:
        c (str): A single character.

    Returns:
        bool: True if the character is lowercase, False otherwise.
    """
    return True if ord(c) in range(97, 123) else False
