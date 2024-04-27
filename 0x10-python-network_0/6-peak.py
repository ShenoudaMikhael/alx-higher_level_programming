#!/usr/bin/python3
"""find peak int module"""


def find_peak(list_of_integers):
    """find peak int"""
    nums = list_of_integers
    n = len(nums)

    # Edge cases
    if n == 0:
        return None
    if n == 1:
        return nums[0]

    # Check if first or last element is a peak
    if nums[0] >= nums[1]:
        return nums[0]
    if nums[n - 1] >= nums[n - 2]:
        return nums[n - 1]

    # Check all elements except the first and last
    for i in range(1, n - 1):
        if nums[i] >= nums[i - 1] and nums[i] >= nums[i + 1]:
            return nums[i]

    # If no peak is found
    return None
