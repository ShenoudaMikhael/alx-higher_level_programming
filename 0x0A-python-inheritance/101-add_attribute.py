#!/usr/bin/python3
"""Module declaration"""


def add_attribute(obj, name, value):
    """adds a new attribute to an object"""
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
