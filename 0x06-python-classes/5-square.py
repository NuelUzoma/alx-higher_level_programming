#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """A class for the square size and computing the area"""

    def __init__(self, _Square__size=0):
        self._Square__size = _Square__size

    def area(self):
        """This instance is to return the area of he square"""
        return _self._Square__size ** 2

    @property
    def size(self):
        """This instance retrives the getter property"""
        return self._Square__size

    @size.setter
    def size(self, value):
        """This instance retrieves the setter property"""
        self._Square__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")

    def my_print(self):
        """This is a public instance with a conditional statement"""
        if (self._Square__size == 0):
            print()
        else:
            for i in range(self._Square__size):
                print("#" * self._Square__size)
