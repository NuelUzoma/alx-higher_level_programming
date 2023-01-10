#!/usr/bin/python3
"""Write a function that returns True if the object
        is exactly an instance of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    if not isinstance(obj, a_class):
        return True
    else:
        return False
    return(obj, a_class)
