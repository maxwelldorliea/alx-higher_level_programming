#!/usr/bin/python3

"""My List Module."""


class MyList(list):
    """Represent custom list type."""

    def print_sorted(self):
        """Print list in sorted order."""
        print(sorted(self))
