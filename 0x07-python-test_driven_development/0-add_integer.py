#!/usr/bin/python3
'''add_integer module'''


def add_integer(a, b=98):
    """
    Adds two integers.
        a: 1st first number.
        b: 2nd number default is 98.
    Returns:
        int: The sum of a and b.
    Raises:
        TypeError: If a or b is not an integer or float.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
