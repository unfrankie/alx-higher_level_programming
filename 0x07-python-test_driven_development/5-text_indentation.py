#!/usr/bin/python3
"""module for text indentation"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    Args:
        text: The input text
    Raises:
        TypeError: If text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sep = [".", "?", ":"]
    current = ""

    for c in text:
        current += c

        if c in sep:
            print(current.strip())
            print()
            current = ""

    if current:
        print(current.strip())
