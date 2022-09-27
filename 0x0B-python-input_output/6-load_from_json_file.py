#!/usr/bin/python3

"""File Json Module."""
import json


def load_from_json_file(filename):
    """Load Json from a file."""
    obj = ""
    with open(filename, "r", encoding="utf-8") as f:
        obj = f.read()

    return json.loads(obj)
