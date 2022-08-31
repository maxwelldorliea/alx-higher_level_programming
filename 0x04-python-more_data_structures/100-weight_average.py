#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0
    w = 0
    sums = 0
    for a, b in my_list:
        sums += a * b
        w += b
    return sums / w
