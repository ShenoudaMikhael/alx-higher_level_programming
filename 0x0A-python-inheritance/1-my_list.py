#!/usr/bin/python3
"""my_list module"""


class MyList(list):
    """My list class"""

    def print_sorted(self) -> None:
        """print the list sorted"""
        if not all(isinstance(x, int) for x in self):
            raise TypeError("all items must be integers")
        a = self.copy()
        a.sort()
        return print(a)
