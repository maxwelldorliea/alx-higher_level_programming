#!/usr/bin/python3

"""File Write Module."""


def write_file(filename="", text=""):
    """Write text to filename."""
    _len = 0
    with open(filename, "w", encoding="utf-8") as f:
        _len = f.write(text)

    return _len
