#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_str = "".join(["{}".format(x) for x in row])
        print(row_str)
