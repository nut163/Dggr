import unittest
from src import terms_conditions

class TestTermsConditions(unittest.TestCase):

    def setUp(self):
        self.terms_conditions = terms_conditions.TermsConditions()

    def test_accept_terms_conditions(self):
        user_id = 1
        self.terms_conditions.acceptTermsConditions(user_id)
        self.assertTrue(self.terms_conditions.checkTermsConditions(user_id))

    def test_decline_terms_conditions(self):
        user_id = 2
        self.terms_conditions.declineTermsConditions(user_id)
        self.assertFalse(self.terms_conditions.checkTermsConditions(user_id))

    def test_terms_conditions_text(self):
        terms_conditions_text = self.terms_conditions.getTermsConditionsText()
        self.assertIsInstance(terms_conditions_text, str)

if __name__ == '__main__':
    unittest.main()