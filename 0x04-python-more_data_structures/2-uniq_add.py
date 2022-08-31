#!/usr/bin/python3


def uniq_add(my_list=[]):
    if not my_list:
        return None
    return sum(set(my_list))
