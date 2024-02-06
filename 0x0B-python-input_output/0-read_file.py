#!/usr/bin/python3
"""Read File Module"""


def read_file(filename=""):
    """
    Reads the contents of a file and prints it to the console.

    Args:
        filename (str, optional): The name of the file to read. Defaults to "".

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as f:
        for i in f.read():
            print(i, end="")
