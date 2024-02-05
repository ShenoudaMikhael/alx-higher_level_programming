#!/usr/bin/python3
""" is same class module """


def is_same_class(obj, a_class):
    """is same class check"""
    return isinstance(obj.__class__, a_class)
