#!/usr/bin/python3
"""
module for creating an object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    create an object from a JSON file
    Args:
        filename: the name of the JSON file
    """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


if __name__ == "__main__":
    load_from_json_file()
