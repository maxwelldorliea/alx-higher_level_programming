#!/usr/bin/python3

"""Matrix Multiplication Module."""

import numpy as np


def is_all_number(matrix, msg):
    """Check if an array is of type number(int/float)."""
    is_number = True
    for arr in matrix:
        for ele in arr:
            if type(ele) not in [int, float]:
                is_number = False
                break
        else:
            continue
        break

    if not is_number:
        raise TypeError(msg)


def lazy_matrix_mul(m_a, m_b):
    """Return the product of two matrix."""
    if not type(m_a) is list:
        raise TypeError("m_a must be a list")
    if not type(m_b) is list:
        raise TypeError("m_b must be a list")

    if not all(isinstance(ele, list) for ele in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(ele, list) for ele in m_b):
        raise TypeError("m_b must be a list of lists")

    if not len(m_a) or all(len(arr) == 0 for arr in m_a):
        raise ValueError("m_a can't be empty")
    if not len(m_b) or all(len(arr) == 0 for arr in m_b):
        raise ValueError("m_b can't be empty")

    is_all_number(m_a, "m_a should contain only integers or floats")
    is_all_number(m_b, "m_b should contain only integers or floats")

    first_len_a = len(m_a[0])
    if not all(first_len_a == len(arr) for arr in m_a):
        raise TypeError("each row of m_a must be of the same size")
    first_len_b = len(m_b[0])
    if not all(first_len_b == len(arr) for arr in m_b):
        raise TypeError("each row of m_b must be of the same size")

    M = len(m_a[0])

    if M != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    a = np.array(m_a)
    b = np.array(m_b)
    
    res = a @ b
    ans = res.tolist()

    return ans
