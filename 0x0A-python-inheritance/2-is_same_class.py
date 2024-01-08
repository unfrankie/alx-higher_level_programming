#!/usr/bin/python3
"""
module for is_same_class function
"""


def is_same_class(obj, a_class):
    """
    return True if the object is exactly an instance of the specified class
    otherwise False.
    Args:
    obj: the object to check
    a_class: the class to compare with
    """
    return type(obj) is a_class
