#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unit tests for the max_integer function
    """

    def test_max_integer(self):
        """
        Tests the function max_integer() with different inputs.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_none_list(self):
        """
        If none list is passed to the function it should return None.
        """
        self.assertEqual(max_integer(), None)


if __name__ == "__main__":
    unittest.main()
