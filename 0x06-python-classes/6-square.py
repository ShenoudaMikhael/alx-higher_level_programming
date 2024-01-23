#!/usr/bin/python3
"""square module docs"""


class Square:
    """Empty Sqaure Class"""

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        return self.__position

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

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.size == 0:
            print("")
            return
        for i in range(self.size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")

            print("")
