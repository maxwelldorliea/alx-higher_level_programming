#!/usr/bin/python3

"""Read File Module."""


def read_file(filename=""):
    """Read and print the content of a text to the standard output."""
    with open(filename, 'r', encoding='UTF-8') as f:
        print(f.read())
