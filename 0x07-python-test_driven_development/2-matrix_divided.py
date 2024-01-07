#!/usr/bin/python3
'''matrix divided module'''


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.
    Args:
        matrix: matrix of numbers
        div: divisor
    Returns:
        list of lists: New matrix with elements divided by div.
    Raises:
        TypeError: if matrix is not a list of lists of integers/floats
                   or if each row of the matrix does not have the same size
                   or if div is not a number
        ZeroDivisionError: if div is equal to 0
    """

    er = "matrix must be a matrix /(list of lists) of integers/floats"
    if not all(
        isinstance(r, list) and all(isinstance(el, (int, float)) for el in r)
        for r in matrix
    ):
        raise TypeError(er)

    if any(len(r) != len(matrix[0]) for r in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result = [[round(el / div, 2) for el in r] for r in matrix]

    return result
