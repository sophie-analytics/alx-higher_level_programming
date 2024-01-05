#!/usr/bin/python3
def uniq_add(my_list=[]):
    num_sum = 0
    for num in set(my_list):
        num_sum += num
    return num_sum
