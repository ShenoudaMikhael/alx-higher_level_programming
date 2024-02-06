#!/usr/bin/python3
"""Studen Class Module"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """
        Init function
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a JSON representation of the object
        """
        return self.__dict__
