#!/usr/bin/python3


def multiply_list_map(my_list=[], number=0):
    if my_list is None:
        return None
    if not my_list:
        return []
    return list(map(lambda x: x * number, my_list))
