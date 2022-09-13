#!/usr/bin/python3


"""creates a new type of type  Square."""


class Square:
    """creates a new type of type  Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square type."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Get the field position value."""
        return self.__position

    @position.setter
    def position(self, position):
        """Set the field position value."""
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Compute the area of a square."""
        return self.__size ** 2

    def my_print(self):
        """Print the a physical representation of the square."""
        if not self.size:
            print()
            return
        for i in range(self.size):
            s = ''
            if self.position[0] > 0:
                s += ' ' * self.position[0]
            s += '#' * self.size
            print(s)
