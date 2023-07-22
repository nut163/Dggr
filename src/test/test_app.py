import unittest
from app import App
from user_profile import UserProfile
from dog_profile import DogProfile

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = App()
        self.user_profile = UserProfile()
        self.dog_profile = DogProfile()

    def test_login(self):
        self.assertEqual(self.app.login('test_username', 'test_password'), 'login_success')

    def test_register(self):
        self.assertEqual(self.app.register('test_username', 'test_password', 'test_email'), 'register_success')

    def test_logout(self):
        self.assertEqual(self.app.logout(), 'logout_success')

    def test_deleteAccount(self):
        self.assertEqual(self.app.deleteAccount('test_username', 'test_password'), 'account_deleted')

    def test_updateUserProfile(self):
        self.assertEqual(self.app.updateUserProfile(self.user_profile), 'profile_updated')

    def test_updateDogProfile(self):
        self.assertEqual(self.app.updateDogProfile(self.dog_profile), 'profile_updated')

    def test_findMatch(self):
        self.assertEqual(self.app.findMatch(), 'match_found')

    def test_startChat(self):
        self.assertEqual(self.app.startChat('test_username', 'test_dogname'), 'chat_started')

    def test_updateSettings(self):
        self.assertEqual(self.app.updateSettings('test_username', 'test_settings'), 'settings_updated')

    def test_updateSubscription(self):
        self.assertEqual(self.app.updateSubscription('test_username', 'test_subscription'), 'subscription_updated')

    def test_clickAd(self):
        self.assertEqual(self.app.clickAd('test_ad_id'), 'ad_clicked')

    def test_updateLocation(self):
        self.assertEqual(self.app.updateLocation('test_username', 'test_location'), 'location_updated')

    def test_swipe(self):
        self.assertEqual(self.app.swipe('test_username', 'test_dogname', 'right'), 'swipe_made')

    def test_receiveNotification(self):
        self.assertEqual(self.app.receiveNotification('test_username'), 'notification_received')

    def test_submitReport(self):
        self.assertEqual(self.app.submitReport('test_username', 'test_report'), 'report_submitted')

    def test_submitReview(self):
        self.assertEqual(self.app.submitReview('test_username', 'test_review'), 'review_submitted')

    def test_makePayment(self):
        self.assertEqual(self.app.makePayment('test_username', 'test_payment'), 'payment_made')

    def test_acceptPrivacyPolicy(self):
        self.assertEqual(self.app.acceptPrivacyPolicy('test_username'), 'privacy_policy_accepted')

    def test_acceptTermsConditions(self):
        self.assertEqual(self.app.acceptTermsConditions('test_username'), 'terms_conditions_accepted')

    def test_requestHelp(self):
        self.assertEqual(self.app.requestHelp('test_username'), 'help_requested')

    def test_changeTheme(self):
        self.assertEqual(self.app.changeTheme('test_username', 'test_theme'), 'theme_changed')

    def test_changeLanguage(self):
        self.assertEqual(self.app.changeLanguage('test_username', 'test_language'), 'language_changed')

    def test_submitFeedback(self):
        self.assertEqual(self.app.submitFeedback('test_username', 'test_feedback'), 'feedback_submitted')

    def test_installUpdate(self):
        self.assertEqual(self.app.installUpdate('test_username'), 'update_installed')

if __name__ == '__main__':
    unittest.main()