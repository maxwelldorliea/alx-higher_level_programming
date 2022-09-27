#!/usr/bin/python3

"""File Json Module."""


class Student:
    """Represent Student Object."""

    def __init__(self, first_name, last_name, age) -> None:
        """Initilize Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Convert the class to json."""
        return self.__dict__
