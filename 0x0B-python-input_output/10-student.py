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
        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()


if __name__ == "__main__":
    pass
