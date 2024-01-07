#!/usr/bin/python3
"""Unittest for max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        '''
        Test max integer
        '''

        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

        self.assertIsNone(max_integer([]))

        self.assertEqual(max_integer([5]), 5)

        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

        self.assertEqual(max_integer([-1, 10, -3, 7]), 10)

        self.assertEqual(max_integer([1.5, 2.7, 3.1, 2.5]), 3.1)

        self.assertEqual(max_integer([-5, -8, -2, -3]), -2)


if __name__ == '__main__':
    unittest.main()
