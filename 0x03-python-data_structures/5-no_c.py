#!/usr/bin/python3

def no_c(my_string):
    result = " "
    for alphabet in my_string:
        if alphabet == 'c' or alphabet == 'C':
            result += ""
        else:
            result += alphabet
    return result