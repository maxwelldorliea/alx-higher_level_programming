#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    new_set = set()
    for item in set_1:
        if item not in set_2:
            new_set.add(item)
    for value in set_2:
        if value not in set_1:
            new_set.add(value)
    return new_set
