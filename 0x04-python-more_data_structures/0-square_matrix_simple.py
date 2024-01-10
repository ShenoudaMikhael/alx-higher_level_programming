#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """return square of matrix"""
    if len(matrix) > 0:
        return [[row[i] ** 2 for i in range(len(row))] for row in matrix]
