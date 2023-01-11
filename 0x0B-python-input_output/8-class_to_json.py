#!/usr/bin/python3
"""Write a function that returns the dictionary description with simple data
        structure (list, dictionary, string, integer and boolean) for
        JSON serialization of an object"""


def class_to_json(obj):
    """The instance"""
    data = {}

    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            data[attr] = value
    return data
