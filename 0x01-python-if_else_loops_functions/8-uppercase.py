#!/usr/bin/python3

def uppercase(str):
    ans = ""
    for s in str:
        if ord(s) >= 97 and ord(s) <= 122:
            ans += chr((ord(s) - 32))
        else:
            ans += s
    print("{0}".format(ans))
