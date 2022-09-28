#!/usr/bin/python3

"""Input Output Module."""


def append_after(filename="", search_string="", new_string=""):
    """Append new_string if search_string is found."""
    cnt = ""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            cnt += line
            if search_string in line:
                cnt += new_string
    with open(filename, "w", encoding="utf-8") as f:
        f.write(cnt)
