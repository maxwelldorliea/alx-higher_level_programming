#!/usr/bin/python3

"""File Json Module."""
import json


def from_json_string(my_str):
    """Return the object representation of a json."""
    return json.loads(my_str)
