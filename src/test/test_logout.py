import unittest
from src.logout import logout

class TestLogout(unittest.TestCase):

    def setUp(self):
        self.user_id = "test_user"

    def test_logout_success(self):
        response = logout(self.user_id)
        self.assertEqual(response, "logout_success")

    def test_logout_failure(self):
        response = logout("invalid_user")
        self.assertNotEqual(response, "logout_success")

if __name__ == '__main__':
    unittest.main()