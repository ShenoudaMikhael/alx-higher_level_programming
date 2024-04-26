#!/usr/bin/python3
"""find peak int module"""


def find_peak(list_of_integers):
    """find peak int"""
    if not list_of_integers:
        return None
    temp = list_of_integers[len(list_of_integers) - 1]

    for i in range(int(len(list_of_integers) / 2)):

        tmax = max(
            list_of_integers[i], list_of_integers[
                len(list_of_integers) - 1 - i])
        temp = tmax if tmax > temp else temp
    return temp
