#!/usr/bin/python3
def uppercase(str1):
    """
    convert str1 to uppercaseand print.

    Args:
        str1 (str1): text.

    Returns:
        None
    """
    for s in str1:
        if ord(s) >= 97 and ord(s) <= 122:
            s = chr(ord(s) - 32)
        print("{}".format(s), end="")
    print("")
