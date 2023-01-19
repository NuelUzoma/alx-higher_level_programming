#!/usr/bin/python3
"""Create a file named models/base.py:
        Class Base:
        private class attribute __nb_objects = 0
        class constructor: def __init__(self, id=None)::
        if id is not None, assign the public instance attribute id with this
        argument value - you can assume id is an integer and
        you don’t need to test the type of it
        otherwise, increment __nb_objects and assign
        the new value to the public instance attribute id"""

import json


class Base:
    """The class Base with a private class attribute and class constructor"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The class constructor containing an ID"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json.dumps(list_dictionaries)
