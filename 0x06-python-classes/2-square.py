#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """A class with a private instance attribute"""
    pass

    def __init__(self, _Square__size):
        """This contains the Square size"""
        self._Square__size = _Square__size

    def __init__(self, _Square__size=0):
        """This contains conditions for the size of the square"""
        self._Square__size = _Square__size
        if not isinstance(_Square__size, int):
            raise TypeError("size must be an integer")
        elif (_Square__size < 0):
            raise ValueError("size must be >= 0")
