#!/usr/bin/python3
"""A unittest python file to test for al methods in the base class"""


import unittest
import json
from models.base import Base, Rectangle


class TestBase(unittest.TestCase):
    """The Test for the class Base"""
    def test_init(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(3)
        self.assertEqual(b2.id, 3)
        b3 = Base(9)
        self.assertEqual(b3.id, 9)

    def test_save_to_file(self):
        rec1 = Rectangle(2, 5, 4, 8)
        rec2 = Rectangle(5, 5, 6, 5)
        list_rectangles = [rec1, rec2]
        Rectangle.save_to_file(list_rectangles)
        with open("Rectangle.json", 'r') as f:
            list_dict = json.load(f)
        ob1 = list_dict[0]
        ob2 = list_dict[1]
        self.assertEqual(ob1["id"], 1)
        self.assertEqual(ob1["width"], 2)
        self.assertEqual(ob2["height"], 5)
        self.assertEqual(ob2["y"], 5)
