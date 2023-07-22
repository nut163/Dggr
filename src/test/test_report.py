import unittest
from src.report import submitReport

class TestReport(unittest.TestCase):

    def setUp(self):
        self.report_id = 1
        self.user_id = 123
        self.report_text = "This user is spamming."

    def test_submit_report(self):
        response = submitReport(self.report_id, self.user_id, self.report_text)
        self.assertEqual(response, 'report_submitted')

if __name__ == '__main__':
    unittest.main()