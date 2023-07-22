```python
from src.database import Database
from src.user_profile import UserSchema
from src.dog_profile import DogSchema

class Report:
    def __init__(self, report_id, user_id, dog_id, report_text):
        self.report_id = report_id
        self.user_id = user_id
        self.dog_id = dog_id
        self.report_text = report_text

    def submit_report(self):
        db = Database()
        user = db.get_user(self.user_id)
        dog = db.get_dog(self.dog_id)

        if user and dog:
            report_data = {
                'report_id': self.report_id,
                'user_id': self.user_id,
                'dog_id': self.dog_id,
                'report_text': self.report_text
            }
            db.insert_report(report_data)
            return 'report_submitted'
        else:
            return 'report_failed'

def report_form(report_id, user_id, dog_id, report_text):
    report = Report(report_id, user_id, dog_id, report_text)
    return report.submit_report()
```