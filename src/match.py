```python
from src.database import Database
from src.dog_profile import DogProfile
from src.user_profile import UserProfile

class Match:
    def __init__(self, match_id, user_id, dog_id):
        self.match_id = match_id
        self.user_id = user_id
        self.dog_id = dog_id
        self.db = Database()

    def find_match(self):
        user = UserProfile(self.user_id)
        dog = DogProfile(self.dog_id)

        potential_matches = self.db.query(DogProfile.DogSchema, {'breed': dog.breed, 'age': dog.age})

        for potential_match in potential_matches:
            if potential_match.user_id != self.user_id:
                return potential_match

        return None

    def save_match(self, match):
        self.db.insert(Match.MatchSchema, {'match_id': self.match_id, 'user_id': self.user_id, 'dog_id': match.dog_id})

    def get_matches(self):
        return self.db.query(Match.MatchSchema, {'user_id': self.user_id})

    def delete_match(self, match_id):
        self.db.delete(Match.MatchSchema, {'match_id': match_id})
```