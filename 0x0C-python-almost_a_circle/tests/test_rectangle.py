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

if __name__ == '__main__':
    unittest.main()
