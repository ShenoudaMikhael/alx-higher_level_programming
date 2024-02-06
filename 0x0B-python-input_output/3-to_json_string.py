#!/usr/bin/python3
"""To JSON Module"""
import json


def to_json_string(obj):
    """
    This function converts the given object to a JSON string.

    Args:
        obj (object): The object to convert to a JSON string.

    Returns:
        str: The JSON string representation of the given object.

    """
    return json.dumps(obj)
