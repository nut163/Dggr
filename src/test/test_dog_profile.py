import unittest
from src.dog_profile import DogSchema, updateDogProfile

class TestDogProfile(unittest.TestCase):

    def setUp(self):
        self.dog_id = "123"
        self.dog_data = {
            "name": "Fido",
            "age": 3,
            "breed": "Labrador",
            "gender": "Male",
            "bio": "Loves long walks in the park.",
            "photos": ["photo1.jpg", "photo2.jpg"]
        }
        self.dog_schema = DogSchema()

    def test_update_dog_profile(self):
        result = updateDogProfile(self.dog_id, self.dog_data)
        self.assertEqual(result, "profile_updated")

    def test_dog_schema(self):
        data = self.dog_schema.load(self.dog_data)
        self.assertEqual(data, self.dog_data)

if __name__ == '__main__':
    unittest.main()