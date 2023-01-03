#!/usr/bin/python3
"""Write a class Rectangle that defines by: (based on 3-rectangle.py)"""


class Rectangle:
    """A class Rectangle that defines a rectangle"""
    def __init__(self, _Rectangle__width=0, _Rectangle__height=0):
        self._Rectangle__height = _Rectangle__height
        self._Rectangle__width = _Rectangle__width

    def area(self):
        """This instance defines the area"""
        return self._Rectangle__height * self._Rectangle__width

    def perimeter(self):
        """This instance defines the pereimeter"""
        if (self._Rectangle__height == 0 or self._Rectangle__width == 0):
            return (0)
        else:
            return 2 * (self._Rectangle__height + self.Rectangle__width)

    def __str__(self):
        """The __str__ instance"""
        if (self._Rectangle__height == 0 or self._Rectangle__width == 0):
            return ''
        return '\n'.\
            join(['#' * self._Rectangle__width] * self._Rectangle__height)

    def __repr__(self):
        """The __repr__ instance to return a string representation"""
        return f'Rectangle(_Rectangle__width={self._Rectangle__width},\
        _Rectangle__height={self._Rectangle__height})'

    @property
    def height(self):
        """The private instance attribute with getter"""
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """The private instance attribute with setter"""
        self._Rectangle__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """The private instance attribute with getter"""
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """The private instance attribute with setter"""
        self._Rectangle__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
