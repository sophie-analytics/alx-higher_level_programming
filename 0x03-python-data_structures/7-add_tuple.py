#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    result_list = []

    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    else:
        tuple_a = tuple_a[:2]

    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
    else:
        tuple_b = tuple_b[:2]

    for value in range(2):
        result_list.append(tuple_a[value] + tuple_b[value])

    result_tuple = tuple(result_list)
    return result_tuple

