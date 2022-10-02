#!/usr/bin/python3

"""Base Class Module."""


class Base:
    """Serve as the base class of all classes."""

    __nb_objects = 0

    def __init__(self, id = None) -> None:
        """Initialize the base class."""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
