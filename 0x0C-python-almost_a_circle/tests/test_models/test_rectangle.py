import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

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

    def test_init(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(r.id, 5)

    def test_init_errors(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2, 3, 4, 5)
        with self.assertRaises(ValueError):
            Rectangle(0, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, "2", 3, 4, 5)
        with self.assertRaises(ValueError):
            Rectangle(1, 0, 3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3", 4, 5)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4", 5)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -1, 5)

    def test_width_setter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.width = 6
        self.assertEqual(r.width, 6)
        with self.assertRaises(TypeError):
            r.width = "6"
        with self.assertRaises(ValueError):
            r.width = 0

    def test_height_setter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.height = 6
        self.assertEqual(r.height, 6)
        with self.assertRaises(TypeError):
            r.height = "6"
        with self.assertRaises(ValueError):
            r.height = 0

    def test_x_setter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.x = 6
        self.assertEqual(r.x, 6)
        with self.assertRaises(TypeError):
            r.x = "6"
        with self.assertRaises(ValueError):
            r.x = -1

    def test_y_setter(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.y = 6
        self.assertEqual(r.y, 6)
        with self.assertRaises(TypeError):
            r.y = "6"
        with self.assertRaises(ValueError):
            r.y = -1


if __name__ == "__main__":
    unittest.main()
