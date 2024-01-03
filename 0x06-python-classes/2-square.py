#!/usr/bin/python3
""" a class module """


class Square:
    """ class that creates a private attribute """
    def __init__(self, size=0):
        """ Constructor:
        Args:
        size: size of a square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
