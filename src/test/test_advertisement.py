import unittest
from src.advertisement import Advertisement

class TestAdvertisement(unittest.TestCase):

    def setUp(self):
        self.advertisement = Advertisement()
        self.ad_id = 1

    def test_clickAd(self):
        response = self.advertisement.clickAd(self.ad_id)
        self.assertEqual(response, 'ad_clicked')

    def test_getAd(self):
        ad = self.advertisement.getAd(self.ad_id)
        self.assertIsNotNone(ad)

    def test_updateAd(self):
        new_ad_data = {'title': 'New Ad', 'description': 'This is a new ad'}
        response = self.advertisement.updateAd(self.ad_id, new_ad_data)
        self.assertEqual(response, 'ad_updated')

    def test_deleteAd(self):
        response = self.advertisement.deleteAd(self.ad_id)
        self.assertEqual(response, 'ad_deleted')

if __name__ == '__main__':
    unittest.main()