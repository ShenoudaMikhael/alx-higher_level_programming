#!/usr/bin/python3
"""find peak int module"""


def div(list_of_ints, low, high):
    """div the array and search"""

    mid = int((high + low) / 2)
    if list_of_ints[mid - 1] <= list_of_ints[mid] >= list_of_ints[mid + 1]:
        return list_of_ints[mid]
    elif list_of_ints[mid] > list_of_ints[mid + 1]:
        return div(list_of_ints, low, mid - 1)
    elif list_of_ints[mid] < list_of_ints[mid + 1]:
        return div(list_of_ints, mid + 1, high)


def find_peak(list_of_integers):
    """Find peak of a list"""

    if not list_of_integers:
        return None
    return div(list_of_integers, 0, len(list_of_integers) - 1)
