#!/usr/bin/python3

"""File Json Module."""


class Student:
    """Represent Student Object."""

    def __init__(self, first_name, last_name, age) -> None:
        """Initilize Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Convert the class to json."""
        if type(attrs) is list and all(type(it) is str for it in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all Student value with json value."""
        for k, v in json.items():
            self.__dict__[k] = v
