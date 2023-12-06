#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for key in a_dictionary:
        new[key] = 2 * a_dictionary[key]
    return new
