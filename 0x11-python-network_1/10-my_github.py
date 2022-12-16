#!/usr/bin/python3
"""Request ALX SE MOdule."""
import requests
from requests.auth import HTTPBasicAuth
import sys


def main() -> None:
    """Take your GitHub credentials (username and password) and."""
    """Use the GitHub API to display your id."""
    cred = HTTPBasicAuth(username=sys.argv[1], password=sys.argv[2])
    res = requests.get('https://api.github.com/user', auth=cred)
    obj = res.json()
    print(obj.get('id'))


if __name__ == '__main__':
    main()
