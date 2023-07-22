import unittest
from src.register import register

class TestRegister(unittest.TestCase):

    def setUp(self):
        self.valid_user_data = {
            'username': 'test_user',
            'password': 'test_password',
            'email': 'test_user@example.com'
        }
        self.invalid_user_data = {
            'username': '',
            'password': '',
            'email': 'invalid_email'
        }

    def test_register_success(self):
        response = register(self.valid_user_data)
        self.assertEqual(response['message'], 'register_success')
        self.assertIsNotNone(response['user_id'])

    def test_register_failure(self):
        response = register(self.invalid_user_data)
        self.assertEqual(response['message'], 'register_failure')

if __name__ == '__main__':
    unittest.main()