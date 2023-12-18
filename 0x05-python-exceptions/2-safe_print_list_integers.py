#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
        count = 0
        try:
            for value in range(x):
                if type(my_list[value]) == int:
                    print("{}".format(my_list[value]), end='')
                    count += 1
        except ValueError as e:
            pass
        print()
        return count
