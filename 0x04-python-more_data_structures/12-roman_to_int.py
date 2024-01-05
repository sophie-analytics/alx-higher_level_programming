#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return None
    roman_no = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    for roman in roman_string:
        number += roman_no[roman]
    return number
