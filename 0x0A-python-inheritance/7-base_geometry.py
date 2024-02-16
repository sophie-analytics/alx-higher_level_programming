#!/usr/bin/python3
"""defines class BaseGeometry"""


class BaseGeometry:
    """ representation of the class """
    def area(self):
        """  defines the area of a geometry"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ checks if a value is an int or string """
        self.name = name
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        self.value = value
