#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        first_char = sentence[:1]
        string_length = None
    else:
        first_char = sentence[:1]
        string_length = len(sentence)
    result = (string_length, first_char, )
    return result 