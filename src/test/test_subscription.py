import unittest
from src.subscription import updateSubscription

class TestSubscription(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.subscription_id = 1

    def test_update_subscription(self):
        response = updateSubscription(self.user_id, self.subscription_id)
        self.assertEqual(response, 'subscription_updated')

if __name__ == '__main__':
    unittest.main()