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

    def __eq__(self, other) -> bool:
        """Check if two object are equal."""
        return self.area() == other.area()

    def __ne__(self, other) -> bool:
        """Check if two object are not equal."""
        return self.area() != other.area()

    def __lt__(self, other) -> bool:
        """Check if one object is less than the other."""
        return self.area() < other.area()

    def __gt__(self, other) -> bool:
        """Check if one object is greater than the other."""
        return self.area() > other.area()

    def __le__(self, other) -> bool:
        """Check if one object is less than or equal to the other."""
        return self.area() <= other.area()

    def __ge__(self, other) -> bool:
        """Check if one object is greater than or equal to the other."""
        return self.area() >= other.area()
