#!/usr/bin/python3
""" my_list module """


class MyList(list):
    """My list class"""

    def print_sorted(self) -> str:
        """print the list sorted"""
        a = self.copy()
        a.sort()
        return print(a)
