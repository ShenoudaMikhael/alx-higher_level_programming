#!/usr/bin/python3
"""Rectangle Module"""
from .base import Base


class Rectangle(Base):
    """Rectangle Class inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")

        if height <= 0:
            raise ValueError("height must be > 0")

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        if not isinstance(y, int):
            raise TypeError("y must be an integer")

        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """get property value"""

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get property value"""

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get property value"""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """get property value"""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of this rectangle."""
        return self.height * self.width

    def display(self):
        """Display the rectangle's information."""
        for _y in range(self.y):
            print("")
        for _ in range(self.height):
            for _x in range(self.x):
                print(" ", end="")
            for __ in range(self.width):

                print("#", end="")
            print("")

    def __str__(self) -> str:
        """
        Return a string representation of the object.
        """

        return "[{}] ({}) {}/{} - {}/{}".format(
            self.__class__.__name__,
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """Update properties using keyword arguments."""
        if args:
            i = args[0] if len(args) > 0 else None
            if i is not None:
                setattr(self, "id", i)

            width = args[1] if len(args) > 1 else None
            if width is not None:
                setattr(self, "width", width)
            height = args[2] if len(args) > 2 else None
            if height is not None:
                setattr(self, "height", height)
            x = args[3] if len(args) > 3 else None
            if x is not None:
                setattr(self, "x", x)
            y = args[4] if len(args) > 4 else None
            if y is not None:
                setattr(self, "y", y)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns a dictionary representation of the object"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
