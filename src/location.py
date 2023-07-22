```python
import geopy
from geopy.distance import geodesic
from src.database import Database
from src.dog_profile import DogSchema

class Location:
    def __init__(self, user_id):
        self.user_id = user_id
        self.db = Database()
        self.dog_schema = DogSchema()

    def get_user_location(self):
        user_data = self.db.get_user_data(self.user_id)
        return user_data['location']

    def update_location(self, new_location):
        self.db.update_user_data(self.user_id, 'location', new_location)
        return {'message': 'location_updated'}

    def get_nearby_dogs(self, radius=5):
        user_location = self.get_user_location()
        all_dogs = self.db.get_all_data('dogs')
        nearby_dogs = []

        for dog in all_dogs:
            dog_owner = self.db.get_user_data(dog['owner_id'])
            dog_location = dog_owner['location']
            distance = geodesic(user_location, dog_location).miles

            if distance <= radius:
                dog_data = self.dog_schema.dump(dog)
                nearby_dogs.append(dog_data)

        return nearby_dogs
```