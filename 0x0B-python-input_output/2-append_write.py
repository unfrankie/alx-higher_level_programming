#!/usr/bin/python3
"""
module for appending a string to the end of a text file UTF8
"""


def append_write(filename="", text=""):
    """
    append a string to a text file and returns the
    number of characters added.
    Args:
        filename: the name of the text file
        text: the string to be appended to the file
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)


if __name__ == "__main__":
    append_write()
