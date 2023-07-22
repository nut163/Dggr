import unittest
from src.match import findMatch

class TestMatch(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.dog_id = 1

    def test_find_match(self):
        match = findMatch(self.user_id, self.dog_id)
        self.assertIsNotNone(match)
        self.assertEqual(match['user_id'], self.user_id)
        self.assertEqual(match['dog_id'], self.dog_id)

    def test_match_not_found(self):
        with self.assertRaises(ValueError):
            findMatch(999, 999)

if __name__ == '__main__':
    unittest.main()