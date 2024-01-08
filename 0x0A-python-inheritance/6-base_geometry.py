#!/usr/bin/python3
"""
module for BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class with an unimplemented area method
    """

    def area(self):
        """
        raises an Exception with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")
