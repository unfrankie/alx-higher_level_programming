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

    def integer_validator(self, name, value):
        """
        validate an integer value
        Args:
        name: a string representing the name of the value
        value: the value to validate
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
