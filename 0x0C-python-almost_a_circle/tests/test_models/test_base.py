#!/usr/bin/python3
"""Base Class Unit test"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Class to represent the TestBase class"""

    def test_init(self):
        Base._Base__nb_objects = 0
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        obj4 = Base(12)
        obj5 = Base("A")
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)
        self.assertEqual(obj4.id, 12)
        self.assertEqual(obj5.id, "A")

    def test_from_json_string(self):
        Base._Base__nb_objects = 0

        json_string = '[{"id": 1}]'
        obj_list = Base.from_json_string(json_string)
        self.assertEqual(obj_list, [{"id": 1}])

    def test_create(self):
        Base._Base__nb_objects = 0

        dictionary = {"id": 1}
        obj = Base.create(**dictionary)
        self.assertEqual(obj.id, 1)


if __name__ == "__main__":
    unittest.main()
