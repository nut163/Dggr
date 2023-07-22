import unittest
from src.login import login

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.user_id = "test_user"
        self.password = "test_password"

    def test_login_success(self):
        response, message = login(self.user_id, self.password)
        self.assertEqual(response, True)
        self.assertEqual(message, "login_success")

    def test_login_failure(self):
        response, message = login(self.user_id, "wrong_password")
        self.assertEqual(response, False)
        self.assertNotEqual(message, "login_success")

if __name__ == '__main__':
    unittest.main()