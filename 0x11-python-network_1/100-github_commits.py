#!/usr/bin/python3
"""Request ALX SE MOdule."""
import requests
import sys


def main() -> None:
    """Print all commits by: `<sha>: <author name>` (one by line)."""
    user = sys.argv[2]
    repo = sys.argv[1]
    query = {'per_page': 10}
    url = f'https://api.github.com/repos/{user}/{repo}/commits'
    res = requests.get(url, params=query)
    objs = res.json()

    for obj in objs:
        commit = obj['commit']
        author = commit['author']
        print(f"{obj.get('sha')}:", author.get('name'))


if __name__ == '__main__':
    main()
