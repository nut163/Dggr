import unittest
from src import delete_account

class TestDeleteAccount(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.delete_account = delete_account.DeleteAccount(self.user_id)

    def test_delete_account(self):
        result = self.delete_account.deleteAccount()
        self.assertEqual(result, 'account_deleted')

    def test_user_id(self):
        self.assertEqual(self.delete_account.user_id, self.user_id)

if __name__ == '__main__':
    unittest.main()