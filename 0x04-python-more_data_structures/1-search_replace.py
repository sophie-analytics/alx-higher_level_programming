#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_new = [replace if item == search else item for item in my_list]
    return list_new
