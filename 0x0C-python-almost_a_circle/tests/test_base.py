import unittest
from models.base import Base

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

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_base_task1(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        b3 = Base()
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)

if __name__ == '__main__':
    unittest.main()
