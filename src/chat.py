```python
import uuid
from src.database import Database
from src.user_profile import UserProfile
from src.dog_profile import DogProfile

class Chat:
    def __init__(self):
        self.chat_id = str(uuid.uuid4())
        self.database = Database()
        self.user_profile = UserProfile()
        self.dog_profile = DogProfile()

    def startChat(self, user_id, dog_id):
        user = self.user_profile.getUser(user_id)
        dog = self.dog_profile.getDog(dog_id)
        if user and dog:
            chat_data = {
                'chat_id': self.chat_id,
                'user_id': user_id,
                'dog_id': dog_id,
                'messages': []
            }
            self.database.insert('chats', chat_data)
            return 'chat_started'
        else:
            return 'user_or_dog_not_found'

    def sendMessage(self, user_id, dog_id, message):
        chat = self.database.find_one('chats', {'user_id': user_id, 'dog_id': dog_id})
        if chat:
            chat['messages'].append({
                'sender': user_id,
                'message': message
            })
            self.database.update('chats', {'chat_id': chat['chat_id']}, chat)
            return 'message_sent'
        else:
            return 'chat_not_found'

    def getMessages(self, user_id, dog_id):
        chat = self.database.find_one('chats', {'user_id': user_id, 'dog_id': dog_id})
        if chat:
            return chat['messages']
        else:
            return 'chat_not_found'
```