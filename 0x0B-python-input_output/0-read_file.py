#!/usr/bin/python3
""" Function that reads the content of the file """
def read_file(filename=""):
    """ args:
    filename: The name of the file to be read"""
    with open(filename,'r', encoding="utf-8") as f:
        data = f.read()
    print(data)
