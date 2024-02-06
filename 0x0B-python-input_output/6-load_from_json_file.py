#!/usr/bin/python3
""" Load from Json Module """
import json


def load_from_json_file(filename):
    """
    This function loads the given JSON file into a Python object.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The Python object loaded from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
