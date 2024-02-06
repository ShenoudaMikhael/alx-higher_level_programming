#!/usr/bin/python3
"""Write File Module """


def write_file(filename="", text=""):
    """
    Writes the contents of a file.

    Args:
        filename (str, optional): The name of the file to write. Defaults to "".
        text (str, optional): The text to write to the file. Defaults to "".

    Returns:
        int: The number of characters written to the file.
    """
    i = 0
    with open(filename, "w", encoding="utf-8") as f:
        i = f.write(text)
    return i
