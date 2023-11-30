#!/usr/bin/python3
def uppercase(str):
    for alphabet in str:
        if ord(alphabet) in range(97, 122):
            alphabet = chr(ord(alphabet) - 32)
        print("{:s}".format(alphabet), end='')
    print()
