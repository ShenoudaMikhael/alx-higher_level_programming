#!/usr/bin/python3
"""divide matrix by a number"""


def matrix_divided(matrix, div):
    """
    Function to divide each element of the matrix by a given number.
    Args:
        matrix (list[list]): The input matrix.
        div (int or float): The divisor.
    Returns:
        list[list]: A new matrix with all elements divided by 'div'.
    Raises:
        TypeError: If 'matrix' is not a matrix or 'div' is not numeric.
        ValueError: If 'div' is zero.
    """
    if not all(
        [
            isinstance(x, int)
            or isinstance(x, float)
            for row in matrix for x in row
            ]
    ):
        raise TypeError(
            "matrix must be a matrix"
            + " (list of lists) of integers/floats")

    for _, row in enumerate(matrix):
        if len(matrix[0]) != len(row):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) or not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
