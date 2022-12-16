#!/usr/bin/python3
"""Request ALX SE MOdule."""
import requests
import sys


def main() -> None:
    """Send a request to the URL and displays the body of the response."""
    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print('Error code:', res.status_code)
    else:
        print(res.text)


if __name__ == '__main__':
    main()
