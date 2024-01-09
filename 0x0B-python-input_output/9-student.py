#!/usr/bin/python3
"""
module for Student class
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

    def to_json(self):
        """
        Retrieve a dictionary representation of a Student instance
        """
        return self.__dict__


if __name__ == "__main__":
    pass
