#!/usr/bin/python3
"""Write a function that returns the list of available 
        attributes and methods of an object
        It returns a LIST object
        No module is to be imported
        Prototype: def lookup(obj)"""

class obj:
    """ """
    pass
    def __init__(self, attr):
        """ """
        self.attr = attr

    def lookup(obj):
        """The prototype function which will return a list object"""
        pass

n = obj(2)
n.lookup()

print(dir(n))
print(dir(obj))
