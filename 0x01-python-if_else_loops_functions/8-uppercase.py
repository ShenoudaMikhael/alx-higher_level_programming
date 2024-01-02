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
        if ord(s) in range(97, 123):
            s = chr(ord(s) - 32)

        print("{}".format(s), end="")

    print("")
