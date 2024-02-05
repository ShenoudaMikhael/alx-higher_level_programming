#!/usr/bin/python3
""" inherits from module """


def inherits_from(obj, a_class):
    """inherits from function"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
