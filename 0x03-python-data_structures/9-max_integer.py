#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        max = my_list[0]
        for value in my_list:
            if value > max:
                max = value
        return max
    
