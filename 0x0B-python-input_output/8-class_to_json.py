#!/usr/bin/python3
"""
module for converting an instance of a class to a JSONserializable dictionary
"""


def class_to_json(obj):
    """
    return the dictionary description for JSON serialization of an object
    Args:
        obj: instance of a class
    """
    return obj.__dict__


if __name__ == "__main__":
    class_to_json()
