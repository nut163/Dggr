import unittest
from src import help_support

class TestHelpSupport(unittest.TestCase):

    def setUp(self):
        self.help_support = help_support.HelpSupport()

    def test_requestHelp(self):
        response = self.help_support.requestHelp("How to create a dog profile?")
        self.assertEqual(response, "Help requested for: How to create a dog profile?")

    def test_getHelpSupportText(self):
        text = self.help_support.getHelpSupportText()
        self.assertTrue(isinstance(text, str))

    def test_updateHelpSupportText(self):
        new_text = "Updated help and support text."
        self.help_support.updateHelpSupportText(new_text)
        self.assertEqual(self.help_support.getHelpSupportText(), new_text)

if __name__ == '__main__':
    unittest.main()