import unittest
from src.language import changeLanguage

class TestLanguage(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.language = 'Spanish'

    def test_change_language(self):
        result = changeLanguage(self.user_id, self.language)
        self.assertEqual(result, 'language_changed')

if __name__ == '__main__':
    unittest.main()