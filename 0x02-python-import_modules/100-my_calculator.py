#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def main():
    argc = len(argv) - 1

    if argc == 0:
        print("{}".format(argc))
        return

    if argv[2] == "+":
        print("{} + {} = {}".format(argv[1], argv[3], add(int(argv[1]), int(argv[3]))))

    elif argv[2] == "-":
        print("{} - {} = {}".format(argv[1], argv[3], sub(int(argv[1]), int(argv[3]))))

    elif argv[2] == "*":
        print("{} * {} = {}".format(argv[1], argv[3], mul(int(argv[1]), int(argv[3]))))

    elif argv[2] == "/":
        print("{} / {} = {}".format(argv[1], argv[3], div(int(argv[1]), int(argv[3]))))


if __name__ == "__main__":
    main()
