import unittest
from src.database import Database
from src.user_profile import UserProfile
from src.dog_profile import DogProfile

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database()
        self.user_profile = UserProfile(user_id="123", name="John Doe", email="johndoe@example.com")
        self.dog_profile = DogProfile(dog_id="456", name="Fido", breed="Labrador", age=3)

    def test_add_user(self):
        self.db.add_user(self.user_profile)
        self.assertIn(self.user_profile, self.db.users)

    def test_add_dog(self):
        self.db.add_dog(self.dog_profile)
        self.assertIn(self.dog_profile, self.db.dogs)

    def test_get_user(self):
        self.db.add_user(self.user_profile)
        retrieved_user = self.db.get_user(self.user_profile.user_id)
        self.assertEqual(retrieved_user, self.user_profile)

    def test_get_dog(self):
        self.db.add_dog(self.dog_profile)
        retrieved_dog = self.db.get_dog(self.dog_profile.dog_id)
        self.assertEqual(retrieved_dog, self.dog_profile)

    def test_delete_user(self):
        self.db.add_user(self.user_profile)
        self.db.delete_user(self.user_profile.user_id)
        self.assertNotIn(self.user_profile, self.db.users)

    def test_delete_dog(self):
        self.db.add_dog(self.dog_profile)
        self.db.delete_dog(self.dog_profile.dog_id)
        self.assertNotIn(self.dog_profile, self.db.dogs)

if __name__ == '__main__':
    unittest.main()