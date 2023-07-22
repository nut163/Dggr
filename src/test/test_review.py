import unittest
from src.review import submitReview

class TestReview(unittest.TestCase):

    def setUp(self):
        self.user_id = "test_user"
        self.dog_id = "test_dog"
        self.review_text = "Great dog!"
        self.rating = 5

    def test_submit_review(self):
        response = submitReview(self.user_id, self.dog_id, self.review_text, self.rating)
        self.assertEqual(response['message'], 'review_submitted')
        self.assertEqual(response['user_id'], self.user_id)
        self.assertEqual(response['dog_id'], self.dog_id)
        self.assertEqual(response['review_text'], self.review_text)
        self.assertEqual(response['rating'], self.rating)

if __name__ == '__main__':
    unittest.main()