#!/usr/bin/python3
"""Write a function that prints a text
        with 2 new lines after each of these characters: ., ? and :
        text must be a string
        otherwise raise a TypeError
        There should be no space at each end of printed line"""


def text_indentation(text):
    """The text indentation function
    text must be a string
    No space allowed at beginning or end"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i, c in enumerate(text):
        if c == '.' or c == '?' or c == ':':
            print(text[i+1:i+3])
        else:
            print(c, end='')
