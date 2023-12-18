#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for num in range(list_length):
        try:
            div = my_list_1[num] / my_list_2[num]
        except (ValueError, TypeError):
            print("wrong type")
            div =  0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            result.append(div)
    return result
