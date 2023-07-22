```python
from src.database import Database
from src.user_profile import UserProfile

class DogProfile:
    def __init__(self, dog_id, user_id, name, breed, age, gender, bio, photo):
        self.dog_id = dog_id
        self.user_id = user_id
        self.name = name
        self.breed = breed
        self.age = age
        self.gender = gender
        self.bio = bio
        self.photo = photo

    def save_to_db(self):
        Database.insert(collection='dogs', data=self.json())

    def json(self):
        return {
            'dog_id': self.dog_id,
            'user_id': self.user_id,
            'name': self.name,
            'breed': self.breed,
            'age': self.age,
            'gender': self.gender,
            'bio': self.bio,
            'photo': self.photo
        }

    @classmethod
    def find_by_user_id(cls, user_id):
        dogs = Database.find(collection='dogs', query={'user_id': user_id})
        return [cls(**dog) for dog in dogs]

    @classmethod
    def find_by_dog_id(cls, dog_id):
        dog = Database.find_one(collection='dogs', query={'dog_id': dog_id})
        return cls(**dog)

    def update_dog_profile(self, name=None, breed=None, age=None, gender=None, bio=None, photo=None):
        if name:
            self.name = name
        if breed:
            self.breed = breed
        if age:
            self.age = age
        if gender:
            self.gender = gender
        if bio:
            self.bio = bio
        if photo:
            self.photo = photo
        self.save_to_db()

    def delete_dog_profile(self):
        Database.delete(collection='dogs', query={'dog_id': self.dog_id})
```