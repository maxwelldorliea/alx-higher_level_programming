#!/usr/bin/python3

"""N Queen Module."""

import sys


def n_queen():
    """Solve n queen puzzle."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        return 1

    col = set()
    posdig = set()
    negdig = set()
    board = [[0] * n for _ in range(n)]
    ans = []

    def backtrack(r):
        """Implement neccessary backtrack."""
        if r == n:
            copy = [row[:] for row in board]
            ans.append(copy)
            return

        for c in range(n):
            if c in col or (r + c) in posdig or (r - c) in negdig:
                continue

            col.add(c)
            posdig.add(r + c)
            negdig.add(r - c)
            board[r][c] = 1

            backtrack(r + 1)
            col.remove(c)
            posdig.remove(r + c)
            negdig.remove(r - c)
            board[r][c] = 0

    def print_result(m):
        """Reorder and print out the result."""
        col = [[[q for q in range(len(i)) if i[q] == 1] for i in a] for a in m]
        for arr in col:
            for r, v in enumerate(arr):
                v.insert(0, r)

        for ans in col:
            print(ans)

    backtrack(0)
    print_result(ans)


n_queen()
