#!/usr/bin/python3
"""Write a function that returns True if the object
        is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False"""


def inherits_from(obj, a_class):
    """The function that will test for a subclass"""
    if issubclass(a_class, a_class):
        return True
    else:
        return False
