#!/usr/bin/python3
""" Checks for an instance of a class"""


def is_kind_of_class(obj, a_class):
    """ function that checks for compatibilty """
    if isinstance(obj, a_class):
        return True
    return False
