#!/usr/bin/python3
"""
Finds a peak in a list of unsorted integers.
"""
def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return None
    peak = list_of_integers[0]
    for i in range(1, len(list_of_integers)):
        if list_of_integers[i] > list_of_integers[i - 1]:
            peak = list_of_integers[i]
    return peak
