#!/usr/bin/python3
"""Write a function that returns the list of available 
        attributes and methods of an object
        It returns a LIST object
        No module is to be imported
        Prototype: def lookup(obj)"""

def lookup(obj):
    """The prototype function which will return a list object"""
    data = dir(obj)
    return data
