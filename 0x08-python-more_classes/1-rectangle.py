#!/usr/bin/python3
""" Class that defines a Rectangle"""
class Rectangle:
    "representation of the class Rectangle"
    def __init__(self, width=0, height=0):
        """ Constructor
            Args: Width: width of the rectangle
            Height: height of the rectangle"""
        self.width = width
        self.height = height
    
    def width(self):
        """ Gets the width of the rectangle"""
        return self.__width
    
    def width(self, value):
        """ Sets the height of the rectangle"""
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__height < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    def height(self):
        return self.__height
    
    def height(self, value):
        """ Sets the height of the rectangle"""
        if not isinstance(self.__height, int):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
