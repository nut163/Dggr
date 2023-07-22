import unittest
from src.feedback import submitFeedback

class TestFeedback(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.feedback = "Great app for dogs to meet!"

    def test_submit_feedback(self):
        response = submitFeedback(self.user_id, self.feedback)
        self.assertEqual(response, 'feedback_submitted')

if __name__ == '__main__':
    unittest.main()