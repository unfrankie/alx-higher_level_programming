#!/usr/bin/python3
def no_c(my_string):
    c_rm = [c for c in my_string if c != 'c' and c != 'C']
    return "".join(c_rm)
