#!/usr/bin/python3
"""Write a function that returns True if the object
        is exactly an instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """The function prototype that returns a boolean"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
