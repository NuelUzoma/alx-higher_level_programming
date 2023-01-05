#!/usr/bin/python3
"""Write a function that adds 2 integers a and b
        The first function describes the function arguments
        The function has two conditional statements
        Checking if it is an integer or a float value
        Also it converts the float values to an integer"""


def add_integer(a, b=98):
    """A function that adds two integers
    a and b and returns the result
    It converts float values also to integers"""

    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return (a + b)
