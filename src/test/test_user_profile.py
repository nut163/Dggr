import unittest
from src.user_profile import UserProfile, UserSchema

class TestUserProfile(unittest.TestCase):

    def setUp(self):
        self.user_profile = UserProfile()
        self.user_data = {
            'user_id': '123',
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'password': 'password123',
            'dog_id': '456',
            'location_id': '789',
            'subscription_id': '321'
        }

    def test_update_user_profile(self):
        self.user_profile.updateUserProfile(self.user_data)
        self.assertEqual(self.user_profile.user_id, '123')
        self.assertEqual(self.user_profile.name, 'John Doe')
        self.assertEqual(self.user_profile.email, 'johndoe@example.com')
        self.assertEqual(self.user_profile.password, 'password123')
        self.assertEqual(self.user_profile.dog_id, '456')
        self.assertEqual(self.user_profile.location_id, '789')
        self.assertEqual(self.user_profile.subscription_id, '321')

    def test_user_schema(self):
        user_schema = UserSchema()
        serialized_data = user_schema.dump(self.user_data)
        self.assertEqual(serialized_data, self.user_data)

if __name__ == '__main__':
    unittest.main()