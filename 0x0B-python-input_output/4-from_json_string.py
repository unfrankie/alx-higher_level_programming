#!/usr/bin/python3
"""
module for returning an object represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    return an object represented by a JSON string
    Args:
        my_str: the JSON string to be converted to an object
    """
    return json.loads(my_str)


if __name__ == "__main__":
    from_json_string()
