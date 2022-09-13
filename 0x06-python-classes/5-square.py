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

    @property
    def size(self):
        """Get the field size value."""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the field size value."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Compute the area of a square."""
        return self.__size ** 2

    def my_print(self):
        """Print the a physical representation of the square."""
        if not self.size:
            print()
            return
        for i in range(self.size):
            s = '#' * self.size
            print(s)
