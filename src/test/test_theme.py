import unittest
from src.theme import changeTheme

class TestTheme(unittest.TestCase):

    def setUp(self):
        self.theme_id = 'dark_mode'
        self.user_id = 'user123'

    def test_change_theme(self):
        result = changeTheme(self.user_id, self.theme_id)
        self.assertEqual(result, 'theme_changed')

if __name__ == '__main__':
    unittest.main()