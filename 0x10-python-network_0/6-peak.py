#!/usr/bin/python3
"""find peak int module"""


def find_peak(list_of_integers):
    """find peak int"""
    if not list_of_integers:
        return None

    n = len(list_of_integers)

    if n == 1:
        return list_of_integers[0]
    elif n == 2:
        return max(list_of_integers)
    else:
        mid = n // 2
        if (
            list_of_integers[mid] > list_of_integers[mid - 1]
            and list_of_integers[mid] > list_of_integers[mid + 1]
        ):
            return list_of_integers[mid]
        elif list_of_integers[mid] < list_of_integers[mid + 1]:
            return find_peak(list_of_integers[mid:])
        else:
            return find_peak(list_of_integers[:mid])
