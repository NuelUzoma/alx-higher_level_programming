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
    if not (isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not (isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]


