#!/usr/bin/python3
"""
matrix multiplication module
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists): The first matrix to multiply.
        m_b (list of lists): The second matrix to multiply with the first.
    """
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all([isinstance(x, list) for x in m_a]):
        raise TypeError("m_a must be a list of lists")
    if not all([isinstance(x, list) for x in m_b]):
        raise TypeError("m_b must be a list of lists")
    if not all(
        [isinstance(x, int) or isinstance(x, float) for row in m_a for x in row]
    ):
        raise TypeError("m_a should contain only integers or floats")
    if not all(
        [isinstance(x, int) or isinstance(x, float) for row in m_b for x in row]
    ):
        raise TypeError("m_b should contain only integers or floats")

    for _, row in enumerate(m_a):
        if len(m_a[0]) != len(row):
            raise TypeError("each row of m_a must be of the same size")

    for _, row in enumerate(m_b):
        if len(m_b[0]) != len(row):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    rows_a = len(m_a)
    cols_a = len(m_a[0])
    cols_b = len(m_b[0])

    for i in range(rows_a):
        row_result = []
        for j in range(cols_b):
            element_sum = 0
            for k in range(cols_a):
                element_sum += m_a[i][k] * m_b[k][j]
            row_result.append(element_sum)
        result.append(row_result)

    return result
