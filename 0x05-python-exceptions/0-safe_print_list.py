def safe_print_list(my_list=[], x=0):
        count = 0
        try:
            for value in range(x):
                print(my_list[value], end='')
                count += 1
        except IndexError as e:
            pass
        print()
        return count
        