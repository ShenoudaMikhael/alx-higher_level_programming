#!/usr/bin/python3
"""Base Module"""
import json
import csv


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
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps([obj for obj in list_dictionaries])

    @classmethod
    def save_to_file(cls, list_objs):
        """Save objects to a file."""

        with open("{}.json".format(cls.__name__),
                  "w+", encoding="utf-8") as file:
            if list_objs is not None:
                file.write(Base.to_json_string(
                    [ob.to_dictionary() for ob in list_objs]))
            else:
                file.write(Base.to_json_string([]))

    @staticmethod
    def from_json_string(json_string):
        """From Json String"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an object from dictionary."""
        # if "size" in dictionary.keys:
        from .rectangle import Rectangle
        from .square import Square

        if "size" in dictionary:
            sqr = Square(size=1)
            sqr.update(**dictionary)
            return sqr

        rct = Rectangle(width=1, height=1)
        rct.update(**dictionary)
        return rct

    @classmethod
    def load_from_file(cls):
        """Load objects from a file."""
        my_list = []
        try:
            with open(
                    "{}.json".format(cls.__name__),
                    "r", encoding="utf-8") as file:
                items = cls.from_json_string(file.read())
                if not items:
                    return my_list
                for item in items:
                    my_list.append(cls.create(**item))
                return my_list
        except FileNotFoundError:
            return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save objects to a file."""
        with open("{}.csv".format(cls.__name__),
                  "w+", encoding="utf-8") as file:
            field_names = []
            if cls.__name__ == "Rectangle":
                field_names = ['id', 'width', 'height', 'x', 'y']
            if cls.__name__ == "Square":
                field_names = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            data = [cls.to_dictionary(item) for item in list_objs]
            writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """Load objects from a file."""
        my_list = []
        try:
            with open(
                "{}.csv".format(cls.__name__),
                    "r", encoding="utf-8") as file:
                q = file.read()

                print(q)
                items = csv.DictReader(file)
                my_list = [cls.create(**dict(row)) for row in items]
            return my_list
        except FileNotFoundError:
            return []
