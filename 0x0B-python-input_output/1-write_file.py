#!/usr/bin/python3
""" Function that write the content into a file """


def write_file(filename="", text=""):
    """ args:
    filename: The name of the file to be read
    text: The text to be written into the file"""
    count = 0
    with open(filename, encoding="utf-8") as f:
        f = f.write(text)
        for ch in f:
            count += 1
    return count
