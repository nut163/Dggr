import unittest
from src import settings

class TestSettings(unittest.TestCase):

    def setUp(self):
        self.user_id = 1
        self.settings = settings.Settings(self.user_id)

    def test_updateSettings(self):
        new_settings = {
            'notifications': True,
            'location_sharing': True,
            'theme': 'dark',
            'language': 'English'
        }
        self.settings.updateSettings(new_settings)
        self.assertEqual(self.settings.settings, new_settings)

    def test_changeTheme(self):
        self.settings.changeTheme('light')
        self.assertEqual(self.settings.settings['theme'], 'light')

    def test_changeLanguage(self):
        self.settings.changeLanguage('Spanish')
        self.assertEqual(self.settings.settings['language'], 'Spanish')

    def test_toggleNotifications(self):
        self.settings.toggleNotifications()
        self.assertEqual(self.settings.settings['notifications'], False)

    def test_toggleLocationSharing(self):
        self.settings.toggleLocationSharing()
        self.assertEqual(self.settings.settings['location_sharing'], False)

if __name__ == '__main__':
    unittest.main()