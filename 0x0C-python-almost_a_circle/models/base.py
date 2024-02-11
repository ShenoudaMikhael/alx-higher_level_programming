#!/usr/bin/python3
"""Base Module"""
import json
import csv
import turtle as t

class Base:
    """Base Geometry Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """To Json string"""
        return json.dumps([obj for obj in list_dictionaries])

    @classmethod
    def save_to_file(cls, list_objs):
        """Save objects to a file."""

        with open("{}.json".format(cls.__name__), "w+", encoding="utf-8") as file:
            file.write(Base.to_json_string([ob.to_dictionary() for ob in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """From Json String"""
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an object from dictionary."""
        # if "size" in dictionary.keys:
        from .rectangle import Rectangle
        from .square import Square

        if "size" in dictionary:
            sqr = Square(size=1)
            sqr.update(*dictionary)
            return sqr

        rct = Rectangle(width=1, height=1)
        rct.update(**dictionary)
        return rct

    @classmethod
    def load_from_file(cls):
        """Load objects from a file."""
        my_list = []
        with open("{}.json".format(cls.__name__), "r", encoding="utf-8") as file:
            items = cls.from_json_string()
            for item in items:
                my_list.append(cls.create(**item))
        return my_list


    def save_to_file_csv(cls, list_objs):
        """Save objects to a file."""

        with open("{}.csv".format(cls.__name__), "w+", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows([ob.to_dictionary() for ob in list_objs])

    def load_from_file_csv(cls):
        """Load objects from a file."""
        my_list = []
        with open("{}.csv".format(cls.__name__), "r", encoding="utf-8") as file:
            items = cls.from_json_string(file)
            for item in items:
                my_list.append(cls.create(**item))
        return my_list
    

    def draw(list_rectangles, list_squares):
        