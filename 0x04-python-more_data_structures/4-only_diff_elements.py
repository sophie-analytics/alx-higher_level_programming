#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_items = []
    for item1 in set_1:
        if item1 not in set_2:
            diff_items.append(item1)
    for item2 in set_2:
        if item2 not in set_1:
            diff_items.append(item2)
    return diff_items
