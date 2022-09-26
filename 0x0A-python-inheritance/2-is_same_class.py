#!/usr/bin/python3

"""Exact Same Object Module."""


def is_same_class(obj, a_class):
    """Check if obj is of type a_class."""
    return isinstance(obj, a_class) and not issubclass(a_class, type(obj))
