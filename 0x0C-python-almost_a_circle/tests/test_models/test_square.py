import unittest
from models.square import Square


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


if __name__ == "__main__":
    unittest.main()
