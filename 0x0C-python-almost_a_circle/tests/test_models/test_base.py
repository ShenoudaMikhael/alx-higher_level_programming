#!/usr/bin/python3
"""Base Class Unit test"""
import unittest
from unittest.mock import patch
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
        obj6 = Base(-2)
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)
        self.assertEqual(obj4.id, 12)
        self.assertEqual(obj5.id, "A")
        self.assertEqual(obj6.id, -2)

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

    @patch("builtins.open", create=True)
    def test_save_to_file(self, mock_open):
        obj = Base()
        obj_list = [obj]
        Base.save_to_file(obj_list)
        mock_open.assert_called_once_with("Base.json", "w+", encoding="utf-8")

    @patch("builtins.open", create=True)
    def test_load_from_file(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = '[{"id": 1}]'
        obj_list = Base.load_from_file()
        self.assertEqual(obj_list[0].id, 1)

    @patch("builtins.open", create=True)
    def test_save_to_file_csv(self, mock_open):
        obj = Base()
        obj_list = [obj]
        Base.save_to_file_csv(obj_list)
        mock_open.assert_called_once_with("Base.csv", "w+", encoding="utf-8")

    @patch("builtins.open", create=True)
    def test_load_from_file_csv(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = '[{"id": 1}]'
        obj_list = Base.load_from_file_csv()
        self.assertEqual(obj_list[0].id, 1)


if __name__ == "__main__":
    unittest.main()
