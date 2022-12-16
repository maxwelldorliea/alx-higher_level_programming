#!/usr/bin/python3

"""Fetch ALX SE Status Module."""
import urllib.request


def main():
    """Fetch https://alx-intranet.hbtn.io/status."""
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        tc_type = type(content)
        utf8 = content.decode()
        output = f"""Body response:
    - type: {tc_type}
    - content: {content}
    - utf8 content: {utf8}"""

    print(output)


if __name__ == '__main__':
    main()
