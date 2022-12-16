#!/usr/bin/python3

"""Fetch ALX SE Status Module."""
import urllib.request


def main():
    """Fetch https://alx-intranet.hbtn.io/status."""
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        byte = res.read()
        content = f"- content: {byte}"
        tc_type = f"- type: {type(content)}"
        utf8 = f"- utf8 content: {byte.decode()}"
        output = "Body response:\n\t{}\n\t{}\n\t{}".format(
                content, tc_type, utf8)

    print(output)


if __name__ == '__main__':
    main()
