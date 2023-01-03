#!/usr/bin/python3
"""Write a class Rectangle that defines by:(based on 5-rectangle.py)"""


class Rectangle:
    """A class Rectangle that defines a rectangle"""
    number_of_instances = 0

    def __init__(self, _Rectangle__width=0, _Rectangle__height=0):
        """An initialization of the class"""
        self._Rectangle__height = _Rectangle__height
        self._Rectangle__width = _Rectangle__width
        Rectangle.number_of_instances += 1

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
        """The __str__ is used for printing the string"""
        if (self._Rectangle__height == 0 or self._Rectangle__width == 0):
            return ''
        return '\n'.\
            join(['#' * self._Rectangle__width] * self._Rectangle__height)

    def __repr__(self):
        """The __repr__ instance returns the string representation"""
        return f'Rectangle(_Rectangle__width={self._Rectangle__width}, \
            _Rectangle__height={self._Rectangle__height})'

    def __del__(self):
        """The __del__ is an instance method"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def height(self):
        """The height getter instance"""
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """The height setter instance"""
        self._Rectangle__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif (value< 0):
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """The width getter instance"""
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """The width setter instance"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif (value< 0):
            raise ValueError("width must be >= 0")

