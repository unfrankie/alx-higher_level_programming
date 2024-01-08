#!/usr/bin/python3
"""
module for MyList class
"""


class MyList(list):
    """
    MyList class that inherits from list
    """

    def print_sorted(self):
        """
        print the list in ascending order
        """
        print(sorted(self))
