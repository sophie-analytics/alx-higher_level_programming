#!/usr/bin/python3
for number in range(100):
    if number < 10:
        print(f"{number:02d},".format(number), end=' ')
    else:
        print(f"{number}".format(number), end=' \n'\
if number == 99 else ', ')
