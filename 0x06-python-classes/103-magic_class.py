#!/usr/bin/python3
"""Create object of type MagicClass."""

import math


class MagicClass:
    """Represent MagicClass."""

    def __init__(self, radius=0) -> None:
        """Initialize the class."""
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """Compute the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Compute the circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
