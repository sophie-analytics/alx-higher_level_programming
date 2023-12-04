#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    no_of_arg = len(argv)
    if no_of_arg == 1:
        print("0 arguments.")
    elif no_of_arg == 2:
        arguments = argv[1:]
        print(f"{no_of_arg - 1} argument:")
        for number in range(no_of_arg - 1):
            print(f"{number + 1}: {arguments[number]}")
    else:
         arguments = argv[1:]
         print(f"{no_of_arg - 1} arguments:")
         for number in range(no_of_arg - 1):
            print(f"{number + 1}: {arguments[number]}")

