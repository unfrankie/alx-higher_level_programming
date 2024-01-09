#!/usr/bin/python3
"""
module for returning the JSON representation of an object
"""


import json


def to_json_string(my_obj):
    """
    return the JSON representation of an object
    Args:
        my_obj: the object to be converted to a JSON string
    """
    return json.dumps(my_obj)


if __name__ == "__main__":
    to_json_string()
