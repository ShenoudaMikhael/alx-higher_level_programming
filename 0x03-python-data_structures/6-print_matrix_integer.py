#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        print("")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(
                "{:d}".format(matrix[i][j]),
                end=" " if j < len(matrix[i]) - 1 else None
            )
