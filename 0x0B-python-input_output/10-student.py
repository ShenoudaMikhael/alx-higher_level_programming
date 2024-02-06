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
        if (isinstance(attrs, list) and all(isinstance(att, str) for att in attrs)):
            return {
                attrib: getattr(self, attrib)
                for attrib in self.__dict__
                if attrib in attrs
            }
        return self.__dict__
