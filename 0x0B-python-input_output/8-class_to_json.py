#!/usr/bin/python3
"""Class to Json Module"""
import json


def class_to_json(obj):
    """
    This function the dictionary description with simple data structure.
    Args:
        obj (object): The Class.
    Returns:
        str: The JSON string representation of the given object.
    """
    return json.dumps(obj.__dict__)
