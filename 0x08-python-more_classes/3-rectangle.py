#!/usr/bin/python3
"""
Rectangle module
"""


class Rectangle:
    """
    rectangle class
    """

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self) -> str:
        if self.__height == 0 or self.__width == 0:
            return ""
        for h in range(self.__height):
            for w in range(self.__width):
                print("#", end="")
            print("")
        return ""

    def __repr__(self) -> str:
        if self.__height == 0 or self.__width == 0:
            return ""
        for _ in range(self.__height):
            for __ in range(self.__width):
                print("#", end="")
            print("", end="" if _ >= self.__height - 1 else None)
        return ""
