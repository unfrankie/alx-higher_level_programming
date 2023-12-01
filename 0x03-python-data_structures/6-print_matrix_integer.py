#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(len(i)):
            x = ' ' if j != len(i) - 1 else ''
            print("{:d}".format(i[j]), end=x)
        print()
