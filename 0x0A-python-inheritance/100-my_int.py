#!/usr/bin/python3
"""defines a class myint that inherits from int"""


class MyInt(int):
    """ reverse the use of == and != """

    def __eq__(self, value):
        """ reverse == """
        return self.real != value

    def __ne__(self, value):
        """ reverse != """
        return self.real == value
