#!/usr/bin/python3
"""
module for Square class
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        initializes a Square instance
        Args:
        size: positive integer representing the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        return a string representation of the Square
        """
        return "[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
