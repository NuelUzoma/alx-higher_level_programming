#!/usr/bin/python3
"""Write a function that appends a string at the end of a
        text file (UTF8) and returns the number of characters added"""


def append_write(filename="", text=""):
    """The function prototype that appends a string at the end"""
    with open('file.append.txt', 'a', encoding="utf-8") as f:
        return f.write(text)
