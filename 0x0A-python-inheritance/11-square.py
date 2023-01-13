#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle
        (9-rectangle.py). (task based on 10-square.py).
        nstantiation with size: def __init__(self, size)::
        size must be private. No getter or setter
        size must be a positive integer, validated by integer_validator
        the area() method must be implemented
        print() should print, and str() should return
        the square description: [Square] <width>/<height>"""


class BaseGeometry:
    """The parent class"""
    def __init__(self):
        """The initialization"""
        pass

    def integer_validator(self, name, value):
        """The integer validator"""
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif (value <= 0):
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """The class Rectangle that defines a rectangle"""
    def __init__(self, width, height):
        """The width and height of the rectangle"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)


class Square(Rectangle):
    """The Square attribute of the class"""
    def __init__(self, size):
        """The size of the square"""
        self.__size = size
        super().integer_validator("size", self.__size)

    def area(self):
        """The area of the Square"""
        return self.__size ** 2

    def __str__(self):
        """The method to print the string"""
        return "[Square] {}/{}".format(self.__size, self.__size)
