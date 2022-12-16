#!/usr/bin/python3
"""Find Peek Module."""


def find_peak(arr):
    """finds a peak in a list of unsorted integer."""
    low = 0
    size = len(arr)
    r = size - 1

    if not arr:
        return
    if size == 1:
        return arr[0]
    if arr[0] >= arr[1]:
        return arr[0]
    if arr[size - 1] >= arr[size - 2]:
        return arr[size - 1]
    while low < r:
        m = low + (r - low) // 2
        if arr[m] <= arr[m + 1]:
            low = m + 1
        else:
            r = m
    return arr[low] if low < len(arr) else arr[low - 1]
