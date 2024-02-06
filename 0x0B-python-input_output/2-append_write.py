#!/usr/bin/python3
""" Append to file Module """


def append_write(filename="", text=""):
    """
    This function appends the given text to the end of the file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters written to the file.

    """
    i = 0
    with open(filename, "a", encoding="utf-8") as f:
        i = f.write(text)
    return i
