#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    sum = 0
    no_of_arg = len(argv) - 1
    arguments = argv[1:]
    for number in range(no_of_arg):
        sum += int(arguments[number])
    print("{}".format(sum))