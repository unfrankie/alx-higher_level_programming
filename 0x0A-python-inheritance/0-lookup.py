#!/usr/bin/python3
"""
Module for lookup function.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object
    Args:
    obj: the object to look up
    """
    return dir(obj)
