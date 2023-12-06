#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [list(map((lambda l: l * l), n)) for n in matrix]
