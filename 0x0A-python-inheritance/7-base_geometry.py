#!/usr/bin/python3
"""Write a class BaseGeometry (based on 6-base_geometry.py).
        Public instance method: def area(self):
        that raises an Exception with the message area() is not implemented
        Public instance method: def integer_validator(self, name, value):
        that validates value:
        you can assume name is always a string
        if value is not an integer: raise a TypeError exception
        with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError exception
        with the message <name> must be greater than 0"""


class BaseGeometry:
    """The class BaseGeometry with two public instance methods"""
    def __init__(self):
        """The initialization of the class"""
        pass

    def area(self):
        """The area of the geometric class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates value"""
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif (value <= 0):
            raise ValueError(f"{name} must be greater than 0")
