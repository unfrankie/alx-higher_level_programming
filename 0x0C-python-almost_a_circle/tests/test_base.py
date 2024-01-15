import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    def test_to_json_string_empty_list(self):
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty_list(self):
        data = [{"id": 1, "name": "example"}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"id": 1, "name": "example"}]')

    def test_from_json_string_empty_string(self):
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_non_empty_string(self):
        data = '[{"id": 1, "name": "example"}]'
        result = Base.from_json_string(data)
        self.assertEqual(result, [{"id": 1, "name": "example"}])

if __name__ == '__main__':
    unittest.main()
