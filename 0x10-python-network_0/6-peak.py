#!/usr/bin/python3
"""find peak int module"""


def find_peak(arr):
    """find peak int"""
    n = len(arr)
    for i in range(1, n - 1):
        if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
            return arr[i]
    return None
