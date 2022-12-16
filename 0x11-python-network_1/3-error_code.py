#!/usr/bin/python3

"""URLLIB ALX SE Module."""
from urllib import request, error
import sys


def main():
    """Send a request to the URL and displays the body of the."""
    """Response (decoded in utf-8)."""
    try:
        with request.urlopen(sys.argv[1]) as res:
            content = res.read()
        print(content.decode())
    except error.HTTPError as e:
        print('Error code:', e.code)


if __name__ == '__main__':
    main()
