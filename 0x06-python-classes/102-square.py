#!/usr/bin/python3
"""square module docs"""


class Square:
    """Empty Sqaure Class"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Square):
            return self.area() == __value.area()

    def __ne__(self, __value: object) -> bool:
        if isinstance(__value, Square):
            return self.area() != __value.area()

    def __le__(self, __value: object) -> bool:
        if isinstance(__value, Square):
            return self.area() <= __value.area()

    def __lt__(self, __value: object) -> bool:
        if isinstance(__value, Square):
            return self.area() < __value.area()

    def __ge__(self, __value: object) -> bool:
        if isinstance(__value, Square):
            return self.area() >= __value.area()

    def __gt__(self, __value: object) -> bool:
        if isinstance(__value, Square):
            return self.area() > __value.area()