#!/usr/bin/python3
"""A Unittest file to test the rectangle class"""


import unittest
import json
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """The test class"""
    def test_init(self):
        r1 = Rectangle(5, 6)
        self.assertEqual(r1.id, 5)
        r2 = Rectangle(2, 10, 0, 5, 6)
        self.assertEqual(r2.id, 6)
        r3 = Rectangle(2, 4)
        self.assertEqual(r3.width, 2)

    def test_str(self):
        r9 = Rectangle(4, 5, 2, 8, 10)
        self.assertEqual(r9.height, 5)

    def test_save_to_file(self):
        rec1 = Rectangle(3, 5, 4, 8)
        rec2 = Rectangle(5, 8, 6, 4)
        list_rectangles = [rec1, rec2]
        Rectangle.save_to_file(list_rectangles)
        with open("Rectangle.json", 'r') as f:
            list_dict = json.load(f)
        ob1 = list_dict[0]
        ob2 = list_dict[1]
        self.assertEqual(ob1["x"], 4)
        self.assertEqual(ob1["width"], 3)
        self.assertEqual(ob2["height"], 8)
        self.assertEqual(ob2["y"], 4)
    
    def test_area(self):
        r4 = Rectangle(9, 3)
        self.assertEqual(r4.area(), 27)
    
    def test_width(self):
        r6 = Rectangle(-10, 10)
        self.assertLessEqual(r6.width, 0)
        with self.assertRaises(ValueError):
            raise ValueError
    
    def test_height(self):
        r5 = Rectangle(9, "3")
        self.assertNotIsInstance(r5.height, int)
        with self.assertRaises(TypeError):
            raise TypeError
    
    def test_x(self):
        r7 = Rectangle(10, 2, -3, 8)
        self.assertLessEqual(r7.x, 0)
        with self.assertRaises(ValueError):
            raise ValueError

    def test_y(self):
        r8 = Rectangle(2, 6, 7, "8")
        self.assertNotIsInstance(r8.y, int)
        with self.assertRaises(TypeError):
            raise TypeError
