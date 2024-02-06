#!/usr/bin/python3
"""Write Files Module"""


def write_file(filename="", text=""):
    """
    Writes the contents of a file.
    """
    i = 0
    with open(filename, "w", encoding="utf-8") as f:
        i = f.write(text)
    return i
