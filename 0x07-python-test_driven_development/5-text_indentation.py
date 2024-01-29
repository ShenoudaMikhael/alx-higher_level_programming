#!/usr/bin/python3
"""
text indentation module
"""


def text_indentation(text):
    """
    Function to add indentations and newlines in a given string.
    It takes the input string, splits
    it into lines based on newline characters,
    adds an indentation of 4 spaces before
    each line except for the first one,
    and then joins them back together with
    newline characters between each line.
    Parameters:
    - text (str): The input string that needs to be indented.
    Returns:
    str: The indented version of the input string.
    Example usage:
    >>> print(text_indentation("This ? is: a test.")
    This?
    <BLANKLINE>
    is
    <BLANKLINE>
    a test.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new = ""
    for c in text.strip():
        if c in ".?:":
            new += c + ("\n\n" if c != text.strip()[-1] else "")
        else:
            if c == " " and new[-3] in ".?:":
                continue
            new += c
    print(new, end="")
