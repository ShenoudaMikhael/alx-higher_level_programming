#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """return square of matrix"""

    return [[row[i] ** 2 for i in range(3)] for row in matrix]