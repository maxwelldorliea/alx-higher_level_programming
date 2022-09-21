#!/usr/bin/python3

"""Text Indentation Module."""


def text_indentation(text):
    """
    Print with rightful Indentation.

    Args:
        text(str): string to be printed

    Raise:
        TypeError: if text is not a string

    Return:
        None
    """
    if not type(text) is str:
        raise TypeError("text must be a string")
    for i, ch in enumerate(text):
        if ch == ' ' and text[i - 1] in ['.', ':', '?']:
            continue
        print(ch, end='')
        if ch in ['.', ':', '?']:
            print("\n")
