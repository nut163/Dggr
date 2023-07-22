```python
class Language:
    def __init__(self):
        self.current_language = 'English'

    def get_current_language(self):
        return self.current_language

    def change_language(self, new_language):
        self.current_language = new_language
        return self.current_language


def changeLanguage():
    language = Language()
    new_language = input("Enter the new language: ")
    language.change_language(new_language)
    print(f"Language changed to {language.get_current_language()}")
```