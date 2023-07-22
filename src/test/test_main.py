import unittest
from src import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = main.create_app()

    def test_app_creation(self):
        self.assertIsNotNone(self.app)

    def test_login(self):
        response = self.app.login(user_id='test_user')
        self.assertEqual(response, 'login_success')

    def test_register(self):
        response = self.app.register(user_id='test_user')
        self.assertEqual(response, 'register_success')

    def test_logout(self):
        response = self.app.logout(user_id='test_user')
        self.assertEqual(response, 'logout_success')

    def test_deleteAccount(self):
        response = self.app.deleteAccount(user_id='test_user')
        self.assertEqual(response, 'account_deleted')

    def test_updateUserProfile(self):
        response = self.app.updateUserProfile(user_id='test_user')
        self.assertEqual(response, 'profile_updated')

    def test_updateDogProfile(self):
        response = self.app.updateDogProfile(dog_id='test_dog')
        self.assertEqual(response, 'profile_updated')

    def test_findMatch(self):
        response = self.app.findMatch(user_id='test_user')
        self.assertEqual(response, 'match_found')

    def test_startChat(self):
        response = self.app.startChat(match_id='test_match')
        self.assertEqual(response, 'chat_started')

    def test_updateSettings(self):
        response = self.app.updateSettings(user_id='test_user')
        self.assertEqual(response, 'settings_updated')

    def test_updateSubscription(self):
        response = self.app.updateSubscription(subscription_id='test_subscription')
        self.assertEqual(response, 'subscription_updated')

    def test_clickAd(self):
        response = self.app.clickAd(ad_id='test_ad')
        self.assertEqual(response, 'ad_clicked')

    def test_updateLocation(self):
        response = self.app.updateLocation(location_id='test_location')
        self.assertEqual(response, 'location_updated')

    def test_swipe(self):
        response = self.app.swipe(user_id='test_user', dog_id='test_dog')
        self.assertEqual(response, 'swipe_made')

    def test_receiveNotification(self):
        response = self.app.receiveNotification(user_id='test_user')
        self.assertEqual(response, 'notification_received')

    def test_submitReport(self):
        response = self.app.submitReport(user_id='test_user')
        self.assertEqual(response, 'report_submitted')

    def test_submitReview(self):
        response = self.app.submitReview(user_id='test_user')
        self.assertEqual(response, 'review_submitted')

    def test_makePayment(self):
        response = self.app.makePayment(user_id='test_user')
        self.assertEqual(response, 'payment_made')

    def test_acceptPrivacyPolicy(self):
        response = self.app.acceptPrivacyPolicy(user_id='test_user')
        self.assertEqual(response, 'privacy_policy_accepted')

    def test_acceptTermsConditions(self):
        response = self.app.acceptTermsConditions(user_id='test_user')
        self.assertEqual(response, 'terms_conditions_accepted')

    def test_requestHelp(self):
        response = self.app.requestHelp(user_id='test_user')
        self.assertEqual(response, 'help_requested')

    def test_changeTheme(self):
        response = self.app.changeTheme(user_id='test_user')
        self.assertEqual(response, 'theme_changed')

    def test_changeLanguage(self):
        response = self.app.changeLanguage(user_id='test_user')
        self.assertEqual(response, 'language_changed')

    def test_submitFeedback(self):
        response = self.app.submitFeedback(user_id='test_user')
        self.assertEqual(response, 'feedback_submitted')

    def test_installUpdate(self):
        response = self.app.installUpdate(user_id='test_user')
        self.assertEqual(response, 'update_installed')

if __name__ == '__main__':
    unittest.main()