#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """A class that contains values for a square and compute the area"""

    def __init__(self, _Square__size=0):
        """This contains the conditional statements"""
        if not isinstance(_Square__size, int):
            raise TypeError("size must be an integer")
        elif (_Square__size < 0):
            raise ValueError("size must be >= 0")
        self._Square__size = _Square__size

    def area(self):
        """This contains the area of the square"""
        return (self._Square__size ** 2)
