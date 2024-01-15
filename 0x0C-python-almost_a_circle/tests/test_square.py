import unittest
from unittest.mock import patch
from models.square import Square
from models.base import Base

class TestSquare(unittest.TestCase):
    def test_size_property(self):
        square = Square(4)
        self.assertEqual(square.size, 4)

    def test_update(self):
        square = Square(4)
        square.update(size=6)
        self.assertEqual(square.size, 6)

    def test_to_dictionary(self):
        square = Square(4, 2, 1, 5)
        result = square.to_dictionary()
        self.assertEqual(result, {'id': 5, 'size': 4, 'x': 2, 'y': 1})

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_square_id_increment(self):
        pass

if __name__ == '__main__':
    unittest.main()
