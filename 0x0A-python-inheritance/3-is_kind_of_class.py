#!/usr/bin/python3
"""
module for is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class;
    otherwise False.
    Args:
    obj: the object to check
    a_class: the class to compare with
    """
    return isinstance(obj, a_class)
