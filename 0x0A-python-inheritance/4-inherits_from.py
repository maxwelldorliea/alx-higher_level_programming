#!/usr/bin/python3

"""Only Sub Class Of Module."""


def inherits_from(obj, a_class):
    """Check if obj is subclass of a_class."""
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
