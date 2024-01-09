#!/usr/bin/python3
"""
module for Student class with filtering
"""


class Student:
    """
    class Student with attributes first_name, last_name, age
    """

    def __init__(self, first_name, last_name, age):
        """
        initialize a Student instance
        Args:
            first_name: the first name of the student
            last_name: the last name of the student
            age: the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieve a dictionary representation of a Student instance
        Args:
            attrs: A list of attributes to include in the dictionary
                         If None, all attributes are included
        """
        if attrs is None or not all(isinstance(attr, str) for attr in attrs):
            return self.__dict__
        return {attr: getattr(self, attr, None) for attr in attrs}


if __name__ == "__main__":
    pass
