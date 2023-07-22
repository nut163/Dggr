import unittest
from src.notification import receiveNotification

class TestNotification(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.notification_id = 1
        self.notification_message = "match_found"

    def test_receiveNotification(self):
        result = receiveNotification(self.user_id, self.notification_id, self.notification_message)
        self.assertEqual(result, "notification_received")

if __name__ == '__main__':
    unittest.main()