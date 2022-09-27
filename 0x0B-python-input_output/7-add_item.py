#!/usr/bin/python3

"""File Json Module."""
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item():
    """Add all arguments to a Python list, and then save them to a file."""
    _len = len(argv)
    mylist = []
    try:
        mylist = load_from_json_file("add_item.json")
    except Exception:
        save_to_json_file(mylist, "add_item.json")
    if _len < 2:
        return
    for i in range(1, _len):
        mylist.append(argv[i])

    save_to_json_file(mylist, "add_item.json")


add_item()
