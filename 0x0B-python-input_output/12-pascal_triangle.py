#!/usr/bin/python3

"""Pascal Triangle Module."""


def pascal_triangle(n):
    """Print Pascal Triangle Layer."""
    if n <= 0:
        return []

    res = [[1]]

    for _ in range(n - 1):
        tmp = [0] + res[-1] + [0]
        row = []

        for j in range(len(res[-1]) + 1):
            row.append(tmp[j] + tmp[j + 1])
        res.append(row)

    return res
