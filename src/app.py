```python
from flask import Flask, request, jsonify
from src.database import db
from src.login import login
from src.register import register
from src.logout import logout
from src.delete_account import deleteAccount
from src.user_profile import updateUserProfile
from src.dog_profile import updateDogProfile
from src.match import findMatch
from src.chat import startChat
from src.settings import updateSettings
from src.subscription import updateSubscription
from src.advertisement import clickAd
from src.location import updateLocation
from src.swipe import swipe
from src.notification import receiveNotification
from src.report import submitReport
from src.review import submitReview
from src.payment import makePayment
from src.privacy_policy import acceptPrivacyPolicy
from src.terms_conditions import acceptTermsConditions
from src.help_support import requestHelp
from src.theme import changeTheme
from src.language import changeLanguage
from src.feedback import submitFeedback
from src.update import installUpdate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

@app.route('/login', methods=['POST'])
def handle_login():
    return login(request.json)

@app.route('/register', methods=['POST'])
def handle_register():
    return register(request.json)

@app.route('/logout', methods=['POST'])
def handle_logout():
    return logout(request.json)

@app.route('/delete_account', methods=['POST'])
def handle_delete_account():
    return deleteAccount(request.json)

@app.route('/update_user_profile', methods=['POST'])
def handle_update_user_profile():
    return updateUserProfile(request.json)

@app.route('/update_dog_profile', methods=['POST'])
def handle_update_dog_profile():
    return updateDogProfile(request.json)

@app.route('/find_match', methods=['POST'])
def handle_find_match():
    return findMatch(request.json)

@app.route('/start_chat', methods=['POST'])
def handle_start_chat():
    return startChat(request.json)

@app.route('/update_settings', methods=['POST'])
def handle_update_settings():
    return updateSettings(request.json)

@app.route('/update_subscription', methods=['POST'])
def handle_update_subscription():
    return updateSubscription(request.json)

@app.route('/click_ad', methods=['POST'])
def handle_click_ad():
    return clickAd(request.json)

@app.route('/update_location', methods=['POST'])
def handle_update_location():
    return updateLocation(request.json)

@app.route('/swipe', methods=['POST'])
def handle_swipe():
    return swipe(request.json)

@app.route('/receive_notification', methods=['POST'])
def handle_receive_notification():
    return receiveNotification(request.json)

@app.route('/submit_report', methods=['POST'])
def handle_submit_report():
    return submitReport(request.json)

@app.route('/submit_review', methods=['POST'])
def handle_submit_review():
    return submitReview(request.json)

@app.route('/make_payment', methods=['POST'])
def handle_make_payment():
    return makePayment(request.json)

@app.route('/accept_privacy_policy', methods=['POST'])
def handle_accept_privacy_policy():
    return acceptPrivacyPolicy(request.json)

@app.route('/accept_terms_conditions', methods=['POST'])
def handle_accept_terms_conditions():
    return acceptTermsConditions(request.json)

@app.route('/request_help', methods=['POST'])
def handle_request_help():
    return requestHelp(request.json)

@app.route('/change_theme', methods=['POST'])
def handle_change_theme():
    return changeTheme(request.json)

@app.route('/change_language', methods=['POST'])
def handle_change_language():
    return changeLanguage(request.json)

@app.route('/submit_feedback', methods=['POST'])
def handle_submit_feedback():
    return submitFeedback(request.json)

@app.route('/install_update', methods=['POST'])
def handle_install_update():
    return installUpdate(request.json)

if __name__ == '__main__':
    app.run(debug=True)
```