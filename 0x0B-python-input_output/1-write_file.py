#!/usr/bin/python3
"""
Module for writing a string to a text file (UTF8).
"""


def write_file(filename="", text=""):
    """
    write a string to a text file and returns the
    number of characters written
    Args:
        filename: the name of the text file
        text: the string to be written to the file
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)


if __name__ == "__main__":
    write_file()
