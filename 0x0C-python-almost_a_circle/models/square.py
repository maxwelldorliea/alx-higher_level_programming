#!/usr/bin/python3

"""Square Module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent an class of type Square."""

    def __init__(self, size, x=0, y=0, id=None) -> None:
        """Initialize a new object of type Square."""
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """Return the string representation of Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the value of the instance field size."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the value of the instance field size."""
        self.width = value

    def update(self, *args, **kwargs):
        """Update the field of an object with either arg variable or kwargs."""
        if args and len(args) > 0:
            for i, v in enumerate(args):
                if i == 0:
                    self.id = v
                elif i == 1:
                    self.width = v
                    self.height = v
                elif i == 2:
                    self.x = v
                elif i == 3:
                    self.y = v
        else:
            for k, v in kwargs.items():
                if k == "size":
                    self.width = v
                    self.height = v
                else:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Return the dictionary representation of an object of type Square."""
        keys = ['id', 'x', 'y', 'size']
        return dict((k, getattr(self, k)) for k in dir(self) if k in keys)
