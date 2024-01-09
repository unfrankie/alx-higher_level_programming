#!/usr/bin/python3
"""
module for writing an object to a text file using a JSON rep
"""


import json


def save_to_json_file(my_obj, filename):
    """
    write an object to a text file using a JSON rep
    Args:
        my_obj: the object to be written to the file
        filename: the name of the text file
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)


if __name__ == "__main__":
    save_to_json_file()
