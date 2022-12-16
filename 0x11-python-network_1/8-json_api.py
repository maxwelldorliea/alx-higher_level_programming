#!/usr/bin/python3
"""Request ALX SE MOdule."""
from json.decoder import JSONDecodeError
import requests
import sys


def main() -> None:
    """Send a POST request to http://0.0.0.0:5000/search_user."""
    param = "" if len(sys.argv) < 2 else sys.argv[1]
    data = {'q': param}
    res = requests.post('http://0.0.0.0:5000/search_user', data=data)

    try:
        obj = res.json()
        if not obj:
            print('No result')
        else:
            print(f"[{obj.get('id')}] {obj.get('name')}")
    except JSONDecodeError:
        print("Not a valid JSON")


if __name__ == '__main__':
    main()
