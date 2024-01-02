#!/usr/bin/python3
def uppercase(str):
    """
    convert str to uppercaseand print.

    Args:
        str (str): text.

    Returns:
        None
    """
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            s = chr(ord(s) - 32)
        print("{}".format(s), end="")
    print("")
