#!/usr/bin/python3
"""Class declaration"""


def add_attribute(obj, name, value):
    """adds a new attribute to an object"""
    if hasattr(obj, "__dict__") == False:
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
