#!/usr/bin/python3
"""Write a class MyList
        that inherits from list
        With a public instance method def print_sorted(self)
        that prints the list
        but sorted in ascending order"""


class MyList(list):
    """The class MyList that inherits from list"""
    def print_sorted(self):
        """The public instance attribute"""
        print(sorted(self))
