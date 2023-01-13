#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry
        (7-base_geometry.py). (task based on 8-rectangle.py)
        the area() method must be implemented
        print() should print, and str() should return
        the following rectangle description: [Rectangle] <width>/<height>"""


class BaseGeometry:
    """The clas BaseGeometry containing methods and a class"""
    def __init__(self):
        """The initialization"""
        pass

    def integer_validator(self, name, value):
        """The method for validating integers"""
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif (value <= 0):
            raise ValueError(f"{name} must be greater than 0")

class Rectangle(BaseGeometry):
    """The class Rectangle which defines a Rectangle"""
    def __init__(self, width, height):
        """The initialization"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)

    def area(self):
        """The implemented area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """The method to print"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
