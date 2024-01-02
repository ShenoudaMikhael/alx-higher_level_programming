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
    for i, s in enumerate(str):
        if ord(str[i]) in range(97, 123):
            str1 += chr(ord(str[i]) - 32)
        else:
            str1 += str[i]
    print(str1)
