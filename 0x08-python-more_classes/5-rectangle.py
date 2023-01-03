#!/usr/bin/python3
"""Write a class Rectangle that defines by: (based on 4-rectangle.py)"""


class Rectangle:
    """A class Rectangle that defines a rectangle"""
    def __init__(self, _Rectangle__width, _Rectangle__height):
        """Initialization of the object"""
        self._Rectangle__height = _Rectangle__height
        self._Rectangle__width = _Rectangle__width

    def area(self):
        """The area of the rectangle"""
        return self._Rectangle__height * self._Rectangle__width

    def perimeter(self):
        """The perimeter of the rectangle"""
        if (self._Rectangle__height == 0 or self._Rectangle__width == 0):
            return (0)
        else:
            return 2 * (self._Rectangle__height + self._Rectangle__width)

    def __str__(self):
        """The __str__ instance property"""
        if (self._Rectangle__height == 0 or self._Rectangle__width == 0):
            return ''
        return '\n'.\
            join(['#' * self._Rectangle__width] * self._Rectangle__height)

    def __repr__(self):
        """The __repr__ instance to print the string representation"""
        return f'Rectangle(_Rectangle__width={self._Rectangle__width}, \
            _Rectangle__height={self._Rectangle__height})'

    def __del__(self):
        """Instance method to check if an instance is deleted"""
        print("Bye rectangle...")

    @property
    def height(self):
        """The getter property of height"""
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """The setter property of height"""
        self._Rectangle__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """The getter property of width"""
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """The setter property of width"""
        self._Rectangle__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= ")
