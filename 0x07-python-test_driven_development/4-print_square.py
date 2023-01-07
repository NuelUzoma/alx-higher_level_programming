#!/usr/bin/python3
"""Write a function that prints a square with the character #
        size is the length of the square
        size must be an integer otherwise raise a TypeError
        size must be >= 0 otherwise raise a ValueError
        size must not be a float"""


def print_square(size):
    """size is the length of the square
    size must be an integer
    size must not be a float and < 0"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif (size < 0):
        raise ValueError("size must be >= 0")
    elif (size == float and size < 0):
        raise TypeError("size must be an integer")
    for i in range(size):
        print('#' * size)
