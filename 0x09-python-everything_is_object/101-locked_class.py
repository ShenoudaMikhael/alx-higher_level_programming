#!/usr/bin/python3
"""
clocked class module
"""


class LockedClass:
    """
    locked class that prevents  direct instantiation
    and provides a lock method to acquire the lock.
    """

    __slots__ = ['first_name']
