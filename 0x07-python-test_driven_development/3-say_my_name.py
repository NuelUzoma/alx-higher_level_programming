#!/usr/bin/python3
"""Write a function that prints
        a first name and a last name
        firstname and lastname must be strings
        otherwise raise a TyoeError
        No module must be imported"""


def say_my_name(first_name, last_name=""):
    """The say_my_name function
    containing two arguments
    firstaname and lastname"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
