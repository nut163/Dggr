import unittest
from src.location import updateLocation, LocationSchema

class TestLocation(unittest.TestCase):

    def setUp(self):
        self.location_id = 1
        self.user_id = 1
        self.dog_id = 1
        self.location_data = {
            'latitude': 40.7128,
            'longitude': 74.0060
        }
        self.location_schema = LocationSchema()

    def test_update_location(self):
        result = updateLocation(self.location_id, self.user_id, self.dog_id, self.location_data)
        self.assertEqual(result['message'], 'location_updated')

    def test_location_schema(self):
        data, errors = self.location_schema.load(self.location_data)
        self.assertFalse(errors)
        self.assertEqual(data['latitude'], self.location_data['latitude'])
        self.assertEqual(data['longitude'], self.location_data['longitude'])

if __name__ == '__main__':
    unittest.main()