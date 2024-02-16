#!/usr/bin/python3
""" Checks if an obj is inherited from a class"""


def inherits_from(obj, a_class):
    """ function that checks"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
