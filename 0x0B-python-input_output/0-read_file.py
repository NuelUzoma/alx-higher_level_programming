#!/usr/bin/python3
"""Write a function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """The function prototype"""
    with open("my_file_0.txt", "r") as f:
        print(f.read(), end="")
