#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    if not set_1 and set_2:
        return set_2
    if not set_2 and set_1:
        return set_1
    if not set_1 and not set_2:
        return None

    return set_1 | set_2
