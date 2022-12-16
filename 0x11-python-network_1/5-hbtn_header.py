#!/usr/bin/python3
"""Request ALX SE MOdule."""
import requests
import sys


def main() -> None:
    """Send a request to the URL and displays the value of the."""
    """Variable X-Request-Id in the response header."""
    res = requests.get(sys.argv[1])
    header = res.headers['X-Request-Id']
    print(header)


if __name__ == '__main__':
    main()
