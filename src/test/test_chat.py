import unittest
from src.chat import Chat, ChatSchema

class TestChat(unittest.TestCase):

    def setUp(self):
        self.chat = Chat()
        self.chat_id = 'chat123'
        self.user_id = 'user123'
        self.dog_id = 'dog123'
        self.message = 'Hello, nice to meet you!'
        self.chat_schema = ChatSchema()

    def test_startChat(self):
        result = self.chat.startChat(self.chat_id, self.user_id, self.dog_id)
        self.assertEqual(result, 'chat_started')

    def test_sendMessage(self):
        result = self.chat.sendMessage(self.chat_id, self.user_id, self.message)
        self.assertEqual(result, 'message_sent')

    def test_receiveMessage(self):
        result = self.chat.receiveMessage(self.chat_id, self.user_id)
        self.assertEqual(result, 'message_received')

    def test_endChat(self):
        result = self.chat.endChat(self.chat_id, self.user_id)
        self.assertEqual(result, 'chat_ended')

    def test_chatSchema(self):
        data = {
            'chat_id': self.chat_id,
            'user_id': self.user_id,
            'dog_id': self.dog_id,
            'message': self.message
        }
        result = self.chat_schema.load(data)
        self.assertEqual(result, data)

if __name__ == '__main__':
    unittest.main()