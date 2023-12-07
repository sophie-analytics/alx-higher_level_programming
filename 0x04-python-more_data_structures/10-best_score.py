#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    
    high_score = 0
    high_key = None
    for key, score in a_dictionary.items():
        if score > high_score:
            high_score = score
            high_key = key
    return high_key
