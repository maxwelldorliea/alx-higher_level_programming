#!/usr/bin/python3

"""Rectangle Module."""
from . import base


class Rectangle(base.Base):
    """Represents reactangle."""

    def __init__(self, width, height, x = 0, y= 0, id=None) -> None:
        """Initialize a reactangle object."""
        super().__init__(id)
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
        self.__width = value

    @property
    def height(self):
        """Get the value of the private instance field height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of the private instance field height."""
        self.__height = value

    @property
    def x(self):
        """Get the value of the private instance field x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of the private instance field x."""
        self.__x = value

    @property
    def y(self):
        """Get the value of the private instance field y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of the private instance field y."""
        self.__y = value
