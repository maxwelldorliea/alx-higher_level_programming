#!/usr/bin/python3

"""Geometry Module."""


class BaseGeometry:
    """Represent a Geometry object."""

    def area(self):
        """Compute the raise of a Geometry object."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if value is a valid integer."""
        if not type(value) is int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
