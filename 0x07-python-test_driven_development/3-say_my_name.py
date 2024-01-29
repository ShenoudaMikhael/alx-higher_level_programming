#!/usr/bin/python3
"""
say my name module
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints out a persons full name.
    Args:
    - first_name (str): The person's first name.
    - last_name (str, optional): The person's last name.
      Defaults to an empty string.

    Raises:
    - TypeError: If the first_name or last_name is not a string.

    Example:
    >>> say_my_name("John", "Doe")
    My name is John Doe
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    return print("My name is {} {}".format(first_name, last_name))
