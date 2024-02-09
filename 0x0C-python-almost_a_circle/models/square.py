#!/usr/bin/python3
"""Rectangle Module"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    A class that represents a square, inheriting from the rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self) -> str:
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        if args:
            i = args[0] if len(args) > 0 else None
            if i is not None:
                setattr(self, "id", i)

            size = args[1] if len(args) > 1 else None
            if size is not None:
                setattr(self, "width", size)
                setattr(self, "height", size)

            x = args[2] if len(args) > 2 else None
            if x is not None:
                setattr(self, "x", x)
            y = args[3] if len(args) > 3 else None
            if y is not None:
                setattr(self, "y", y)
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns a dictionary representation of the object"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y,
        }
