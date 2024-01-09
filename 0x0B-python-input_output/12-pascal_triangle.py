#!/usr/bin/python3
"""
Module for generating Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle of n
    Args:
        n (int): the number of rows to generate
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for _ in range(1, n):
        row = [1]
        for j in range(1, len(triangle[-1])):
            row.append(triangle[-1][j - 1] + triangle[-1][j])
        row.append(1)
        triangle.append(row)

    return triangle


if __name__ == "__main__":
    pass
