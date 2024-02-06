#!/usr/bin/python3
"""Studen Class Module"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and len(attrs) > 0:
            a = {x: getattr(self, x) for x in self.__dict__ if x in attrs}
            return a

        return vars(self)
