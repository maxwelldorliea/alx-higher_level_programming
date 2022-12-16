#!/usr/bin/python3

"""URLLIB ALX SE Module."""
import urllib.request
import sys


def main():
    """Send a request to the URL and displays the value of the X-Request-Id."""
    """Variable found in the header of the respons."""
    with urllib.request.urlopen(sys.argv[1]) as res:
        header = res.getheader("X-Request-Id")
    print(header)


if __name__ == '__main__':
    main()
