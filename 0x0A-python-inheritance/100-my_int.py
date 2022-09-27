#!/usr/bin/python3

"""MyInt Module."""


class MyInt(int):
    """Represent MyInt Object."""

    def __eq__(self, __x: object) -> bool:
        """Return False if two MyInt is equal."""
        return not super().__eq__(__x)

    def __ne__(self, __x: object) -> bool:
        """Return True if two MyInt is equal."""
        return not super().__ne__(__x)
