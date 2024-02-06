#!/usr/bin/python3
"""From Json String Module """
import json


def from_json_string(my_str):
    """
    This function converts the given JSON string to a Python object.

    Args:
        my_str (str): The JSON string to convert to a Python object.

    Returns:
        object: The Python object representation of the given JSON string.

    """
    return json.loads(my_str)
