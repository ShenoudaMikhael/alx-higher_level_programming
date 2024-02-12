import unittest
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):

    def test_init(self):
        square = Square(5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_size(self):
        square = Square(5)
        self.assertEqual(square.size, 5)

    def test_size_setter(self):
        square = Square(5)
        square.size = 7
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)

    def test_str(self):
        square = Square(5, 1, 2, 10)
        self.assertEqual(str(square), "[Square] (10) 1/2 - 5")

    def test_update(self):
        square = Square(5, 1, 1, 10)
        square.update(20, 7, 8, 9)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 9)

    def test_to_dictionary(self):
        square = Square(5, 1, 1, 10)
        square_dict = square.to_dictionary()
        self.assertEqual(square_dict, {"id": 10, "size": 5, "x": 1, "y": 1})

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_initialization(self):
        s = Square(5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_square_initialization_with_x_and_y(self):
        s = Square(5, 3, 4)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_square_initialization_with_id(self):
        s = Square(5, 3, 4, 12)
        self.assertEqual(s.id, 12)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_square_size_getter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_square_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_square_str_representation(self):
        s = Square(5, 3, 4, 12)
        expected = "[Square] (12) 3/4 - 5"
        self.assertEqual(str(s), expected)

    def test_square_update_args(self):
        s = Square(5, 3, 4, 12)
        s.update(15, 10, 1, 2)
        self.assertEqual(s.id, 15)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

    def test_square_update_kwargs(self):
        s = Square(5, 3, 4, 12)
        s.update(id=15, width=10, height=10, x=1, y=2)
        self.assertEqual(s.id, 15)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

    def test_square_to_dictionary(self):
        s = Square(5, 3, 4, 12)
        expected = {
            "id": 12,
            "size": 5,
            "x": 3,
            "y": 4,
        }
        self.assertDictEqual(s.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
