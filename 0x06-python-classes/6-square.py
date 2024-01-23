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

        if not all(isinstance(x, int) and x >= 0 for x in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        pos_x, pos_y = self.position
        for _ in range(pos_y):
            print("")
        if self.size == 0:
            print("")
            return
        for i in range(self.size):
            for _ in range(pos_x):
                print(" ", end="")

            for j in range(self.size):
                print("#", end="")
            print("")
