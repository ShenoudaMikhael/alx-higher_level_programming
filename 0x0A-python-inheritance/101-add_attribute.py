#!/usr/bin/python3
""" 
add attribute module with one function
"""


def add_attribute(obj: object, name: str, value) -> None:
    """
    Add an attribute to an object.

    Args:
        obj (object): The object to which the attribute will be added.
        name (str): The name of the attribute.
        value: The value of the attribute.

    Raises:
        TypeError: If the object does not have a __dict__ attribute.

    Returns:
        None: Does not return any value.
    """
    if hasattr(obj, "__dict__") == False:
        raise TypeError("[TypeError] can't add new attribute")

    setattr(obj, name, value)
