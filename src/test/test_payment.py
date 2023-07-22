import unittest
from src.payment import makePayment

class TestPayment(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.subscription_id = 1
        self.payment_data = {
            'card_number': '1234567812345678',
            'expiry_date': '12/24',
            'cvv': '123',
            'card_holder_name': 'John Doe'
        }

    def test_make_payment(self):
        response = makePayment(self.user_id, self.subscription_id, self.payment_data)
        self.assertEqual(response, 'payment_made')

if __name__ == '__main__':
    unittest.main()