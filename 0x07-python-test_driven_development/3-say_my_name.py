#!/usr/bin/python3

"""Say My Name Module."""


def say_my_name(first_name, last_name=""):
    """
    Print first and last name in a sentence.

    Args:
        first_name(string): first argument
        last_name(string): second argument

    Raise:
        TypeError: if first_name is not a string
        TypeError: if last_name is not a string

    Return:
        None
    """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")

    if not type(last_name) is str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
