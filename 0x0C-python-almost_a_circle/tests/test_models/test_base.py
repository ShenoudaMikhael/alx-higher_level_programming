#!/usr/bin/python3
"""Base Class Unit test"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_to_json_string(self):
        Base._Base__nb_objects = 0

        list_dicts = [{"id": 1}, {"id": 2}, {"id": 3}]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(json_string, '[{"id": 1}, {"id": 2}, {"id": 3}]')

    def test_from_json_string(self):
        Base._Base__nb_objects = 0

        json_string = '[{"id": 1}, {"id": 2}, {"id": 3}]'
        list_dicts = Base.from_json_string(json_string)
        self.assertEqual(len(list_dicts), 3)
        self.assertEqual(list_dicts[0], {"id": 1})
        self.assertEqual(list_dicts[1], {"id": 2})
        self.assertEqual(list_dicts[2], {"id": 3})

    def test_create(self):
        Base._Base__nb_objects = 0

        dictionary = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        rectangle = Base.create(**dictionary)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)

        dictionary = {"id": 2, "size": 4, "x": 5, "y": 6}
        square = Base.create(**dictionary)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 4)
        self.assertEqual(square.x, 5)
        self.assertEqual(square.y, 6)

    def test_load_from_file(self):
        Base._Base__nb_objects = 0

        sqr0 = Square(id=1, size=2, x=3, y=4)
        Square.save_to_file([sqr0])
        sq1 = Square.load_from_file()
        self.assertNotEqual(sq1, sqr0)
        self.assertEqual(len(sq1), 1)
        self.assertEqual(sq1[0].id, 1)
        self.assertEqual(sq1[0].size, 2)
        self.assertEqual(sq1[0].x, 3)
        self.assertEqual(sq1[0].y, 4)

    def test_save_to_file(self):
        Base._Base__nb_objects = 0

        list_rects = [Rectangle(1, 2), Rectangle(3, 4), Rectangle(5, 6)]
        Rectangle.save_to_file(list_rects)
        with open("Rectangle.json", "r", encoding="utf-8") as file:
            saved_rects = Base.from_json_string(file.read())
        self.assertEqual(
            saved_rects,
            [
                {"id": 1, "width": 1, "height": 2, "x": 0, "y": 0},
                {"id": 2, "width": 3, "height": 4, "x": 0, "y": 0},
                {"id": 3, "width": 5, "height": 6, "x": 0, "y": 0},
            ],
        )


if __name__ == "__main__":
    unittest.main()
