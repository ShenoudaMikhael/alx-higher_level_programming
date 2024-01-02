#!/usr/bin/python3
def remove_char_at(str, n):
    """
    This function takes a string and an integer as input.
    It removes the character at position 'n' from the string. If 'n' is
    """
    q = ""
    for i in range(len(str)):
        q += str[i] if i != n else ""
    return q
