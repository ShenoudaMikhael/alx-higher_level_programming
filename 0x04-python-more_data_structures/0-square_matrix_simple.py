#!usr/bin/python3
def square_matrix_simple(matrix=[]):
    """return square of matrix"""
    # new_matrix = [[row[i] ** 2 for i in range(3)] for row in matrix]
    new_matrix = []
    for row in matrix:
        h = []
        for i in range(len(row)):
            h.append(row[i] ** 2)
        new_matrix.append(h)

    return new_matrix
