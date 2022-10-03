#!/usr/bin/python3

"""Rectangle Module."""
from models.base import Base


class Rectangle(Base):
    """Represents reactangle."""

    def __init__(self, width, height, x=0, y=0, id=None) -> None:
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
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
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
            raise ValueError("x must be >= 0")
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
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Compute and return the area of a rectangle."""
        return self.__height * self.__width

    def display(self):
        """Print the shape of the rectangle."""
        [print() for _ in range(self.__y)]
        for _ in range(self.__height):
            print(' ' * self.__x, end='')
            print('#' * self.__width)

    def __str__(self) -> str:
        """Return the string representation of a rectangle object."""
        size = f" - {self.__width}/{self.__height}"
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}{size}"

    def update(self, *args, **kwargs):
        """Update rectangle using arg-var."""
        if args and len(args) > 0:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.width = v
                elif i == 2:
                    self.height = v
                elif i == 3:
                    self.x = v
                elif i == 4:
                    self.y = v
        else:

            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Return the dictionary representation of an object."""
        keys = ['id', 'width', 'height', 'x', 'y']
        return dict((k, getattr(self, k)) for k in dir(self) if k in keys)
