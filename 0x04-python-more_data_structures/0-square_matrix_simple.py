#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Check that the input matrix is a list of lists
    if not all(isinstance(row, list) for row in matrix):
        raise ValueError("Input matrix is not a list of lists")
    squared_matrix = [
            [0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            squared_matrix[i][j] = matrix[i][j]**2
    return squared_matrix
