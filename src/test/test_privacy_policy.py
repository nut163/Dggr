import unittest
from src.privacy_policy import acceptPrivacyPolicy

class TestPrivacyPolicy(unittest.TestCase):

    def setUp(self):
        self.user_id = 1

    def test_accept_privacy_policy(self):
        result = acceptPrivacyPolicy(self.user_id)
        self.assertEqual(result, 'privacy_policy_accepted')

if __name__ == '__main__':
    unittest.main()