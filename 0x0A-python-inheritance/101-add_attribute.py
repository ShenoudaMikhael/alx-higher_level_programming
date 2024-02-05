#!/usr/bin/python3
"""add attribute module"""


def add_attribute(obj, name, value):
    """add attribute functoin"""
    if hasattr(obj, "__dict__") == False:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
