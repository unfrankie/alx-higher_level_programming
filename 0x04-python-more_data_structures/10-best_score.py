#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None
    keys = list(a_dictionary)
    biggest_v = a_dictionary[keys[0]]
    biggest_k = keys[0]
    for key in keys:
        if a_dictionary[key] > biggest_v:
            biggest_v = a_dictionary[key]
            biggest_k = key
    return biggest_k
