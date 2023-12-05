#!/usr/bin/python3
a = 89
b = 10
copy_a = b; b = a
a = copy_a
print("a={:d} - b={:d}".format(a, b))