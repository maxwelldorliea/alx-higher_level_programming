#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):

    for arr in matrix:
        for i in range(len(arr)):
            print("{:d}".format(arr[i]), end="")
            if i != len(arr) - 1:
                print(" ", end="")
        print()
