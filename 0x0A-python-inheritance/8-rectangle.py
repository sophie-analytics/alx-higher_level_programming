#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" subclass inherits from parent class """


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry."""
    def __init__(self, width, height):
        """Intialize a new Rectangle."""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
