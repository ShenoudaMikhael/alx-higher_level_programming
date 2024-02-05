#!/usr/bin/python3
"""base geometry module"""


class BaseGeometry:
    """Base geometry class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if not isinstance(name, str):
            raise Exception("{} is not a string".format(name))

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
