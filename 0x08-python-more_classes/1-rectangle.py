#!/usr/bin/python3

"""Simple Rectangle Module."""


class Rectangle:
    """Represent a Rectangle."""

    def __init__(self, width=0, height=0) -> None:
        """Initialize the an object Rectangle type."""
        if not type(width) is int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not type(height) is int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get the value of width."""
        return self.__width

    @width.setter
    def width(self, val):
        """Set the value of width."""
        self.__width = val

    @property
    def height(self):
        """Get the value of height."""
        return self.__height

    @height.setter
    def height(self, val):
        """Set the value of height."""
        self.__height = val
