import unittest
from src.swipe import swipe

class TestSwipe(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.dog_id = 2
        self.swipe_direction = "right"

    def test_swipe_right(self):
        result = swipe(self.user_id, self.dog_id, self.swipe_direction)
        self.assertEqual(result, "swipe_made")

    def test_swipe_left(self):
        self.swipe_direction = "left"
        result = swipe(self.user_id, self.dog_id, self.swipe_direction)
        self.assertEqual(result, "swipe_made")

    def test_swipe_invalid_direction(self):
        self.swipe_direction = "up"
        result = swipe(self.user_id, self.dog_id, self.swipe_direction)
        self.assertEqual(result, "Invalid swipe direction")

if __name__ == '__main__':
    unittest.main()