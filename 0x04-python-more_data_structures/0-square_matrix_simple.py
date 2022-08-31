#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    new_matrix = []
    for list_ in matrix:
        sub_list = list(map(lambda x: x*x, list_))
        new_matrix.append(sub_list)

    return new_matrix
