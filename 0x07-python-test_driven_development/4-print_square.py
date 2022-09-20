#!/usr/bin/python3


"""Print Square Module."""


def print_square(size):
    """
    Print Square Shape Using Hashtag(#).

    Args:
        size(integer): size of the square
    Raise:
        TypeError: if size is not an integer
        ValueError: if size if less than 0
    Return:
        None
    """
    if not type(size) is int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print('#' * size)
