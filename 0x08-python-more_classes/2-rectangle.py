#!/usr/bin/python3
"""Write a class Rectangle that defines by: (based on 1-rectangle.py)"""


class Rectangle:
    """The class Rectangle that defines a rectangle"""
    def __init__(self, _Rectangle__width=0, _Rectangle__height=0):
        """The initialization of the Rectangle"""
        self._Rectangle__height = _Rectangle__height
        self._Rectangle__width = _Rectangle__width

    def area(self):
        """The area of the Rectangle"""
        return self._Rectangle__height * self._Rectangle__width

    def perimeter(self):
        """The perimeter of the Rectangle"""
        if (self._Rectangle__height == 0 or self._Rectangle__width == 0):
            return (0)
        else:
            return 2 * (self._Rectangle__height + self._Rectangle__width)
    
    @property
    def height(self):
        """The height instance getter"""
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """The height instance setter"""
        self._Rectangle__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """The width instance getter"""
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """The width instance setter"""
        self._Rectangle__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
