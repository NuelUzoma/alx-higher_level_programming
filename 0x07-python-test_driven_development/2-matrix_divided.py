#!/usr/bin/python3
"""Write a function that divides all elements of a matrix
        matrix must be a list of lists of integers or floats
        otherwise raise a TypeError
        Each row of the matrix must be of the same size
        otherwise raise a TypeError"""


def matrix_divided(matrix, div):
    """The function of the matrix
    it took two arguments, matrix and div
    All elements should be divided by div"""
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_sizes = [len(row) for row in matrix]
    if not all(size == row_sizes[0] for size in row_sizes):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) or isinstance(div, float):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    result = [[round(elem / div, 2) for elem in row] for row in matrix]

    return (result)
