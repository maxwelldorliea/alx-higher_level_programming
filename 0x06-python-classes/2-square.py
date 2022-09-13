#!/usr/bin/python3


"""creates a new type of type  Square."""


class Square:
    """creates a new type of type  Square."""

    def __init__(self, size=0):
        """Initialize the square type."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
