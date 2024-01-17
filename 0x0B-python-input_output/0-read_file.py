#!/usr/bin/python3
""" Function that reads the content of the file """
def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        data = f.read()
    print(data)
