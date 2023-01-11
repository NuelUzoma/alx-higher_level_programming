#!/usr/bin/python3
"""Write a function that creates an Object from a “JSON file”"""


import json


def load_from_json_file(filename):
    """The function prototype that creates an Object"""
    with open(filename, 'r') as f:
        data = json.load(f)
        return data
