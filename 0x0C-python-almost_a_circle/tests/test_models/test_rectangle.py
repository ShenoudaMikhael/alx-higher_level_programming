import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_init(self):
        rect = Rectangle(2, 3, 1, 1)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 1)

    def test_area(self):
        rect = Rectangle(2, 3)
        self.assertEqual(rect.area(), 6)

    def test_str(self):
        rect = Rectangle(2, 3, 1, 1, 10)
        self.assertEqual(str(rect), "[Rectangle] (10) 1/1 - 2/3")

    def test_update(self):
        rect = Rectangle(2, 3, 1, 1, 10)
        rect.update(20, 4, 5, 6, 7)
        self.assertEqual(rect.id, 20)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 6)
        self.assertEqual(rect.y, 7)

    def test_to_dictionary(self):
        rect = Rectangle(2, 3, 1, 1, 10)
        rect_dict = rect.to_dictionary()
        self.assertEqual(rect_dict, {"id": 10, "width": 2, "height": 3, "x": 1, "y": 1})


if __name__ == "__main__":
    unittest.main()
