#!/usr/bin/python3
"""Write a class Rectangle that inherits from
        BaseGeometry (7-base_geometry.py).
        Instantiation with width and height:
        def __init__(self, width, height):
        width and height must be private. No getter or setter
        width and height must be positive integers,
        validated by integer_validator"""


class BaseGeometry:
    """Tha class BaseGeometry with methods and a class"""
    def __init__(self):
        """The initialization of the class"""
        pass

    def area(self):
        """The area of the class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """The integer validator of the class"""
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif (value <= 0):
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry"""
    def __init__(self):
        """Initialization"""
        super().__init__(self)
    
    def __init__(self, width, height):
        """The init of the width and height"""
        self.width = width
        self.height = height

    def integer_validator(self, width, height):
        """The integer validator of the class"""
        self.width = width
        self.height = height
        if not isinstance((width, height), int):
            raise TypeError(f"{name} must be an integer")
        elif (width <= 0) or (height <= 0):
            raise ValueError(f"{name} must be greater than 0")
