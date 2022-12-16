#!/usr/bin/python3
"""Request ALX SE MOdule."""
import requests


def main() -> None:
    """Fetch https://alx-intranet.hbtn.io/status."""
    res = requests.get('https://alx-intranet.hbtn.io/status')
    content = res.text
    ct_type = type(content)
    output = f"Body response:\n\t- type: {ct_type}\n\t- content: {content}"
    print(output)


if __name__ == '__main__':
    main()
