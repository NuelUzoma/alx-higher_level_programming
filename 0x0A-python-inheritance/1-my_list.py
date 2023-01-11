#!/usr/bin/python3
"""Write a class MyList 
        that inherits from list
        With a public instance method def print_sorted(self)
        that prints the list
        but sorted in ascending order"""


class list:
    """The parent class which will contain other classes
    All attributes will be initialized from here
    """
    def __init__(self, int):
        self.list = int

    def append(self, int):
        pass

class MyList(list):
    """The MyList inherits from the parent class list """
    def __init__(self):
        """ """
        super().__init__(int)

    def print_sorted(self):
        """Prints the list in a sorted order"""
        data = []
        dat = set(data)
        return dat
