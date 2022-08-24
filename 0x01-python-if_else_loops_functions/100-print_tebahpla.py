#!/usr/bin/python3

s = ""
i = ord('z')
while i >= ord('a'):
    if i % 2:
        s += chr(i - 32)
    else:
        s += chr(i)
    i -= 1
print("{0}".format(s), end="")
