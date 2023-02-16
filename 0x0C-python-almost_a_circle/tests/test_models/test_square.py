#!/usr/bin/python3
"""A umittest test file to test for all methods in the Square Class"""


import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """The test for the class Square from Base"""
    def test_init(self):
        """The test for the init method"""
        s1 = Square(4)
        self.assertEqual(s1.id, 2)
        self.assertEqual(s1.size, 4)

    def test_area(self):
        """The test for the area method"""
        s2 = Square(5)
        self.assertEqual(s2.area(), 25)

    def test_update(self):
        """The test method for the *args  and **kwargs method"""
        pass
