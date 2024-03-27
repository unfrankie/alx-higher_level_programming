#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if list_of_integers:
        length = len(list_of_integers)
        low, high = 0, length - 1
        while low < high:
            middle = (low + high) // 2
            if list_of_integers[middle] > list_of_integers[middle + 1]:
                high = middle
            else:
                low = middle + 1
        return list_of_integers[low]
