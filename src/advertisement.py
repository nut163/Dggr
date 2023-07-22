```python
import uuid
from src.database import Database
from src.user_profile import UserProfile

class Advertisement:
    def __init__(self):
        self.db = Database()
        self.ad_id = str(uuid.uuid4())
        self.user_profile = UserProfile()

    def create_ad(self, ad_content, ad_image):
        ad_data = {
            "ad_id": self.ad_id,
            "ad_content": ad_content,
            "ad_image": ad_image
        }
        self.db.insert("Advertisements", ad_data)

    def click_ad(self, user_id):
        user_data = self.user_profile.get_user_profile(user_id)
        if user_data["subscription_id"] is None:
            self.db.update("Advertisements", {"ad_id": self.ad_id}, {"clicks": "clicks + 1"})
            return "ad_clicked"
        else:
            return "subscription_active"

    def get_ad(self):
        ad_data = self.db.select("Advertisements", {"ad_id": self.ad_id})
        return ad_data
```