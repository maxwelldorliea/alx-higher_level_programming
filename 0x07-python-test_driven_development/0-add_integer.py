#!/usr/bin/python3

"""Compute the the sum of two number."""


def add_integer(a, b=98):
    """
    Add two number a and b.

    Args:
        a(int/float): first number
        b(int/float): second number
    Raise:
        TypeError: if a or b is not int or float
    Return:
        (int): sum of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
