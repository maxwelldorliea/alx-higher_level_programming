#!/usr/bin/python3

"""Read File Module."""


def read_file(filename=""):
    """Read and print the content of a text to the standard output."""
    with open(file=filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
