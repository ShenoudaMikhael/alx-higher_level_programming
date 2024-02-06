#!/usr/bin/python3
"""Save to Json file Module"""
import json


def save_to_json_file(my_obj, filename):
    """
    This function saves the given object to a JSON file.

    Args:
        my_obj (object): The object to save to a JSON file.
        filename (str): The name of the file to save to.

    Returns:
        None
    """
    j = json.dumps(my_obj)
    with open(filename, "w+", encoding="utf-8") as f:
        f.write(j)
