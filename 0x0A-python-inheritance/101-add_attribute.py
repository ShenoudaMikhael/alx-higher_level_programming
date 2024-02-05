#!/usr/bin/python3
"""add attribute module with one function"""


def add_attribute(obj, name, value):
    """
    add attribute function
    args:
        obj: object
        name: name
        value: value
    return:
        NONE
    """
    if hasattr(obj, "__dict__") == False:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
