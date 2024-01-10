#!usr/bin/python3
def square_matrix_simple(matrix=[]):
    """return square of matrix"""
    if len(matrix) > 0:
        new_matrix = [[row[i] ** 2 for i in range(3)] for row in matrix]
        return new_matrix
