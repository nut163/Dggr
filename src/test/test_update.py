import unittest
from src import update

class TestUpdate(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.update_id = 1

    def test_installUpdate(self):
        result = update.installUpdate(self.user_id, self.update_id)
        self.assertEqual(result, 'update_installed')

    def tearDown(self):
        self.user_id = None
        self.update_id = None

if __name__ == '__main__':
    unittest.main()