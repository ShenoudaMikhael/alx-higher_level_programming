#!/usr/bin/python3
"""Magic class calculation"""
import math


class MagicClass:
    """circle magic"""

    def __init__(self, radius=0):
        if (type(radius) is not int) and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        return math.pi * (self.__radius**2)

    def circumference(self):
        return 2 * math.pi * self.__radius
