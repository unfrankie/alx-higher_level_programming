#!/usr/bin/python3
"""
module for inherits_from function
"""


def inherits_from(obj, a_class):
    """
    return True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    Args:
    obj: the object to check
    a_class: the class to compare with
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
