#!/usr/bin/python3
"""Pascal Triangle Module"""


def pascal_triangle(num):
    """pascal trinagle function"""

    list1 = []
    for i in range(num):
        list1.append([])
        list1[i].append(1)
        for j in range(1, i):
            list1[i].append(list1[i - 1][j - 1] + list1[i - 1][j])
        if num != 0 and i > 0:
            list1[i].append(1)

    return list1
