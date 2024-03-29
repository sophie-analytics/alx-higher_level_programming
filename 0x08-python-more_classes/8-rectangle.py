#!/usr/bin/python3
""" Class that defines a Rectangle"""


class Rectangle:
    "representation of the class Rectangle"
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Constructor
            Args: Width: width of the rectangle
            Height: height of the rectangle"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
            for i in range(self.__height - 1):
                for j in range(self.__width):
                    result += str(self.print_symbol)
                result += "\n"
            for k in range(self.__width):
                result += str(self.print_symbol)
            return result

    def __repr__(self):
        """Redefines the repr function """
        return ("{}({}, {})".
                format(self.__class__.__name__, self.__width, self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    def __del__(self):
        """deletes the class """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
