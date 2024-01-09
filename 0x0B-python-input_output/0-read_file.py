#!/usr/bin/python3
"""
Module for reading a text file (UTF8) and printing it to stdout.
"""


def read_file(filename=""):
    """
    read a text file and prints it to stdout

    Args:
        filename: The name of the text file to be read
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")


if __name__ == "__main__":
    read_file()
