#!/usr/bin/python3

"""URLLIB ALX SE Module."""
from urllib import request, parse
import sys


def main():
    """Send a POST request to the passed URL with the email as a parameter."""
    """And displays the body of the response (decoded in utf-8)."""
    body = {'email': sys.argv[2]}
    data = parse.urlencode(body).encode('ascii')
    url = request.Request(sys.argv[1], data)
    with request.urlopen(url) as res:
        content = res.read()
    print(content.decode())


if __name__ == '__main__':
    main()
