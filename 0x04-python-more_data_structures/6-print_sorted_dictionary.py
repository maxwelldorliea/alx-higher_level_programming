#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    if not a_dictionary:
        return
    keys = sorted(a_dictionary)

    for key in keys:
        print("{}: {}".format(key, a_dictionary.get(key)))
