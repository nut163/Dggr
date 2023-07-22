```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    def __init__(self):
        self.database_uri = os.getenv('DATABASE_URI')
        self.secret_key = os.getenv('SECRET_KEY')
        self.mail_server = os.getenv('MAIL_SERVER')
        self.mail_port = os.getenv('MAIL_PORT')
        self.mail_use_tls = os.getenv('MAIL_USE_TLS')
        self.mail_username = os.getenv('MAIL_USERNAME')
        self.mail_password = os.getenv('MAIL_PASSWORD')
        self.ad_server = os.getenv('AD_SERVER')

    def updateSettings(self, new_settings):
        for key, value in new_settings.items():
            setattr(self, key, value)

    def getSettings(self):
        return {
            'database_uri': self.database_uri,
            'secret_key': self.secret_key,
            'mail_server': self.mail_server,
            'mail_port': self.mail_port,
            'mail_use_tls': self.mail_use_tls,
            'mail_username': self.mail_username,
            'mail_password': self.mail_password,
            'ad_server': self.ad_server
        }
```