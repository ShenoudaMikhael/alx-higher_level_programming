#!/usr/bin/python3
"""find peak int module"""


def find_peak(list_of_integers):
    """find peak int"""
    nums = list_of_integers
    array_len = len(nums)

    if array_len == 0:
        return None
    if array_len == 1:
        return nums[0]

    if nums[0] >= nums[1]:
        return nums[0]
    if nums[array_len - 1] >= nums[array_len - 2]:
        return nums[array_len - 1]

    for i in range(1, array_len - 1):
        if nums[i] >= nums[i - 1] and nums[i] >= nums[i + 1]:
            return nums[i]

    return None
