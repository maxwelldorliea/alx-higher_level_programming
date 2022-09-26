#!/usr/bin/python3

"""LooK Up Module."""


def lookup(obj):
    """
    Return list of all method and attribute in an object.

    Args:
        obj(Object) : object whom method and attribute is to be return

    Raise:
        None

    Return:
        List of attributes and methods
    """
    return dir(obj)
