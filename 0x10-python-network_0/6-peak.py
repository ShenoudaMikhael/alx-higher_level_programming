#!/usr/bin/python3
"""find peak int module"""


def find_peak(list_of_integers):
    """find peak int"""
    temp = None
    for i in set(list_of_integers):
        if not temp or temp < i:
            temp = i
    return temp
