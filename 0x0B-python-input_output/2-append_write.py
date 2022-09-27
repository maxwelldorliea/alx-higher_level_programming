#!/usr/bin/python3

"""File Append Module."""


def append_write(filename="", text=""):
    """Create a file if not exist or append to a file."""
    _len = 0
    with open(filename, "a", encoding="utf-8") as f:
        _len = f.write(text)

    return _len
