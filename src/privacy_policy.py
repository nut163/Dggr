```python
class PrivacyPolicy:
    def __init__(self):
        self.privacy_policy_text = "assets/privacy_policy.txt"

    def acceptPrivacyPolicy(self, user_id):
        # Code to update the user's profile to reflect that they have accepted the privacy policy
        pass

    def displayPrivacyPolicy(self):
        with open(self.privacy_policy_text, 'r') as file:
            data = file.read().replace('\n', '')
        return data
```