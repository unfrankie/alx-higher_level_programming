import unittest
from unittest.mock import patch
import io
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        rect = Rectangle(2, 3)
        result = rect.area()
        self.assertEqual(result, 6)

    def test_display(self):
        rect = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            rect.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_update(self):
        rect = Rectangle(2, 3)
        rect.update(width=4, height=5)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)

    def test_to_dictionary(self):
        rect = Rectangle(2, 3, 1, 1, 5)
        result = rect.to_dictionary()
        self.assertEqual(result, {'id': 5, 'width': 2, 'height': 3, 'x': 1, 'y': 1})

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_rectangle(self):
        """ rectangle func """
        #
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        #
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        #12
        r4 = Rectangle(1, 2)
        self.assertEqual(r4.id, 3)
        #13
        r5 = Rectangle(1, 2, 3)
        self.assertEqual(r5.id, 4)
        #14
        r5 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r5.id, 5)
        #15
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        #16
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        #17
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        #18
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        #19
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        #20
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        #21
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        #22
        with self.assertRaises(ValueError):
            Rectangle(0, -2)
        #23
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        #24
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        #25
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)
        #26
        self.assertEqual(Rectangle(3, 2).area(), 6)
        #27
        self.assertEqual(Rectangle(4, 6, 2, 1, 12).__str__(), '[Rectangle] (12) 2/1 - 4/6')

if __name__ == '__main__':
    unittest.main()
