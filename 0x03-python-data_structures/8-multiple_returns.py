#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        first_char = None
        string_length = 0
    else:
        first_char = sentence[:1]
        string_length = len(sentence)
    result = (string_length, first_char, )
    return result 