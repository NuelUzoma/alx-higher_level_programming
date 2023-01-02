#!/usr/bin/python3
""" Write a class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """A class containing the size of a square and instances"""

    def __init__(self, _Square__size=0, position=(0, 0)):
        """The constructor for the square"""
        self._Square__size = _Square__size
        self.position = position

    def area(self):
        """The area of the square"""
        return self._Square__size ** 2

    def my_print(self):
        """This instance prints in stdout the square of #"""
        if (self._Square__size == 0):
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self._Square__size):
                print(" " * self.position[0] + "#" * self._Square__size)

    @property
    def size(self):
        """The instance getter property of the class"""
        return self._Square__size

    @size.setter
    def size(self, value):
        """The instance setter property of the class"""
        self._Square__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """The coordinates of the square"""
        return self._position

    @position.setter
    def position(self, value):
        """The coordinates but with values"""
        self._position = value
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

