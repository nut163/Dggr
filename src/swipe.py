```python
import json
from src.database import Database
from src.dog_profile import DogProfile
from src.match import Match

class Swipe:
    def __init__(self, user_id, dog_id):
        self.user_id = user_id
        self.dog_id = dog_id
        self.db = Database()

    def swipe_right(self):
        # User likes the dog, add to liked dogs
        self.db.update('liked_dogs', {self.user_id: self.dog_id})

        # Check if there's a match
        if self.check_match():
            # Create a new match
            match = Match(self.user_id, self.dog_id)
            match_id = match.create_match()

            # Send a notification to the user
            self.send_notification('match_found', match_id)

    def swipe_left(self):
        # User dislikes the dog, add to disliked dogs
        self.db.update('disliked_dogs', {self.user_id: self.dog_id})

    def check_match(self):
        # Check if the dog also liked the user
        liked_dogs = self.db.get('liked_dogs', self.dog_id)
        return self.user_id in liked_dogs

    def send_notification(self, message_name, match_id):
        # Send a notification to the user
        notification = {
            'user_id': self.user_id,
            'message_name': message_name,
            'match_id': match_id
        }
        self.db.update('notifications', notification)
```