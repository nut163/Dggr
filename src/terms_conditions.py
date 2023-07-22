```python
class TermsConditions:
    def __init__(self):
        self.terms_conditions_text = "assets/terms_conditions.txt"

    def acceptTermsConditions(self, user_id):
        # Update the user's profile to reflect that they have accepted the terms and conditions
        # This is a placeholder and should be replaced with actual database update code
        print(f"User {user_id} has accepted the terms and conditions.")

    def displayTermsConditions(self):
        # Open the terms and conditions file and print its contents
        with open(self.terms_conditions_text, 'r') as file:
            print(file.read())

    def updateTermsConditions(self, new_text):
        # Update the terms and conditions text file with new text
        # This should only be accessible by administrators
        with open(self.terms_conditions_text, 'w') as file:
            file.write(new_text)
            print("Terms and conditions have been updated.")
```