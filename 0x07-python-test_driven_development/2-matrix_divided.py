#!/usr/bin/python3

"""Matrix Division Module."""


def matrix_divided(matrix, div):
    """
    Divides All Element of The Matrix.

    Args:
        matrix(list of list of int/float): first argumunt
        div(int/float): seconde argument

    Raise:
        TypeError: if matrix is not of type (list of lists) of integers/floats
        TypeError: if each row of the matrix are not of the same size
        ZeroDivisionError: if div is 0

    Return:
        (list of list of int/float): modified matrix.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not type(matrix) is list:
        raise TypeError(msg)

    if not all(isinstance(ele, list) for ele in matrix):
        raise TypeError(msg)

    if all(len(arr) == 0 for arr in matrix):
        raise TypeError(msg)

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

    first_arr_len = len(matrix[0])

    if not all(first_arr_len == len(arr) for arr in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not type(div) in [float, int]:
        raise TypeError("div must be a number")
    if not div:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda v: round(v / div, 2), arr)) for arr in matrix]
