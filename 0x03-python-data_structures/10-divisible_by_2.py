#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = [value % 2 == 0 for value in my_list]
    return new_list