#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as err:
        stderr.write('Exception: ')
        stderr.write(str(err))
        stderr.write('\n')
        return None
    return res
