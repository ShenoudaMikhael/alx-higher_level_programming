#!/usr/bin/python3


def uppercase(str):
    """
    convert str to uppercaseand print.

    Args:
        str (str): text.

    Returns:
        None
    """
    str1 = ""
    for s in range(len(str)):
        str1 += chr(ord(
            str[s]) - 32) if ord(str[s]) in range(97, 123) else str[s]
    print(str1)
