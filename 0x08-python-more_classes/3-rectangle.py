#!/usr/bin/python3
""" Class that defines a Rectangle"""


class Rectangle:
    "representation of the class Rectangle"
    def __init__(self, width=0, height=0):
        """ Constructor
            Args: Width: width of the rectangle
            Height: height of the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Defines the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Redefines the str function """
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    result += "#"
                result += "\n"
            return result
