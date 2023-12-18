#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    f_element = 0
    for i in range(x):
        try:
            print('{:d}'.format(my_list[i]), end='')
            f_element += 1
        except (TypeError, ValueError):
            pass
    print()
    return f_element
