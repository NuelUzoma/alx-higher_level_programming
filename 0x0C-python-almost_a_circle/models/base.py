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
from models import Rectangle, Square


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
        if (list_dictionaries is None) or (len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """A method that returns the list of the JSON string representation"""
        if (json_string is None) or (len(json_string) == 0):
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """A class method"""
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)
        with open(filename, 'w') as f:
            f.write(json_string)
