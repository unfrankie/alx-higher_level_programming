#!/usr/bin/python3
"""
module for Rectangle class
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        initialize a Rectangle instance
        Args:
        width: positive integer representing the width
        height: positive integer representing the height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        compute the area of the Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        return a string representation of the Rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
