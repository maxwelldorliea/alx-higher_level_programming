#!/usr/bin/python3

"""Rectangle Module."""
from . import base


class Rectangle(base.Base):
    """Represents reactangle."""

    def __init__(self, width, height, x = 0, y= 0, id=None) -> None:
        """Initialize a reactangle object."""
        super().__init__(id)
        if not type(width) is int:
            raise TypeError("width must be an integer")
        if not type(height) is int:
            raise TypeError("height must be an integer")
        if not type(x) is int:
            raise TypeError("x must be an integer")
        if not type(y) is int:
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be > 0")
        if y < 0:
            raise ValueError("y must be > 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get the value of the private instance field width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of the private instance field width."""
        if not type(value) is int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the value of the private instance field height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of the private instance field height."""
        if not type(value) is int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the value of the private instance field x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of the private instance field x."""
        if not type(value) is int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """Get the value of the private instance field y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of the private instance field y."""
        if not type(value) is int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value
