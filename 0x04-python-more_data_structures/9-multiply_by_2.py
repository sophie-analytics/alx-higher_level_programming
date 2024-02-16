#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return {}
    new_dict = {}
    for key, values in a_dictionary.items():
        new_dict[key] = values * 2
    return new_dict
