#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """A class that returns the current square area of the size"""

    def __init__(self, _Square__size=0):
        """This contains the conditional statement"""
        if not isinstance(_Square__size, int):
            raise TypeError("size must be an integer")
        elif (_Square__size < 0):
            raise ValueError("size must be >= 0")
        self._Square__size = _Square__size

    def area(self):
        """The area pf the square"""
        return self._Square__size ** 2

    @property
    def size(self):
        """The retrieving property"""
        return self._Square__size

    @size.setter
    def size(self, value):
        """The getter property"""
        self._Square__size = value
