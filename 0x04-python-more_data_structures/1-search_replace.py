#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for num in range(len(my_list)):
        if my_list[num] == search:
            my_list[num] = replace
        else:
            new_list.append(my_list[num])
    return new_list
