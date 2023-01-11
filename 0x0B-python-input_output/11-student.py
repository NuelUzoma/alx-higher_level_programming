#!/usr/bin/python3
"""Write a class Student that defines a student by (based on 10-student.py)"""


class Student:
    """The class Student defines a student with firstname, lastname and age"""
    def __init__(self, first_name, last_ame, age):
        """The initiallization of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """It retrieves a dict rep of a student"""
        data = {}
        if attrs is not None and isinstance(attrs, list):
            for attr in attrs:
                if hasattr(self, attr):
                    data[attr] = getattr(self, attr)
        else:
            for attr, value in self.__dict__.items():
                if isinstance(value, (list, dict, str, int, bool)):
                    data[attr] = value
            return data

    def reload_from_json(self, json):
        """It replaces all attributes of the student instance"""
        for attr, value in json.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
