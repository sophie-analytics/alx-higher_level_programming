#!/usr/bin/python3
""" class that prints a list content in sorted manner"""


class MyList(list):
    """ Inherited or Derived class from list class"""  
    def print_sorted(self):
        """ function that sorts the list values(int)"""
        print(sorted(self))
