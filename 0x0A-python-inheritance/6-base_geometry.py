#!/usr/bin/python3
"""Write a class BaseGeometry (based on 5-base_geometry.py).
        Public instance method: def area(self)
        that raises an Exception with the message area() is not implemented"""


class BaseGeometry:
    """A  class that raises an exception of the area"""
    def __init__(self):
        """The initialization of the class"""
        pass

    def area(self):
        """The area of the geometric clss"""
        raise Exception("area() is not implemented")
