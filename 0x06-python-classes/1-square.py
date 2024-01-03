#!/usr/bin/python3
"""  A class that define the size of a square,
a private attribute """


class Square:
    """ object initialization """
    
    def __init__(self, size):
        """Constructor.
        Args:
        size: length of side of the square.
        """
        self.__size = size
