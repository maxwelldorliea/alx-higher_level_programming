#!/usr/bin/python3

"""Square Module."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent Square object."""

    def __init__(self, size):
        """Initialize Square Object."""
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """Compute the area of the Square."""
        return self.__size * self.__size

    def __str__(self) -> str:
        """Return the string representation of Square."""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
