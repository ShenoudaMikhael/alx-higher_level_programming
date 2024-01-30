#!/usr/bin/python3
"""
clocked class module
"""


class LockedClass:
    """
    locked class that prevents  direct instantiation
    and provides a lock method to acquire the lock.
    """

    def __setattr__(self, name, value):
        if not name != "first_name":
            raise AttributeError
