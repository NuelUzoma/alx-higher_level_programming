#!/usr/bin/python3
"""Write a class Student that defines a student by
        first_name of the student
        last_name of the student
        and age of the student
        All as public instance attributes"""


class Student:
    """The class Student containing all the info of the student"""
    def __init__(self, first_name, last_name, age):
        """The initialization of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This method retrieves a dictionary representation
        of a student instance"""
        data = {}
        for attr, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                data[attr] = value
        return data
