#!/usr/bin/python3


def print_last_digit(number):
    flag = 0

    if number < 0:
        flag = 1
        number *= -1
    last = number % 10

    print("{:d}".format(last), end="")
    return last
