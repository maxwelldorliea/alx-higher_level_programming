#!/usr/bin/python3
from sys import argv


def main():
    argc = len(argv) - 1

    if argc == 0:
        print("{} arguments:".format(argc))
        return
    if argc == 1:
        print("{} argument:".format(argc))
        print("{}: {}".format(argc, argv[1]))
        return

    print("{} arguments:".format(argc))

    for i in range(1, argc + 1):
        print("{}: {}".format(argc, argv[i]))


if __name__ == "__main__":
    main()
