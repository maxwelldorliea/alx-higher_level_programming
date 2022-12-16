#!/usr/bin/python3
"""Request ALX SE MOdule."""
import requests
import sys


def main() -> None:
    """Send a POST request to the passed URL with the email as a."""
    """Parameter, and finally displays the body of the response."""
    data = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data)
    print('Your email is:', res.text)


if __name__ == '__main__':
    main()
