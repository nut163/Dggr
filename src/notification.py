```python
import json
from flask import Flask, request
from src.database import Database

app = Flask(__name__)
db = Database()

@app.route('/notification', methods=['POST'])
def receiveNotification():
    data = request.get_json()
    user_id = data['user_id']
    notification_id = data['notification_id']
    message = data['message']

    # Save notification to database
    db.save_notification(user_id, notification_id, message)

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

@app.route('/notification/<notification_id>', methods=['GET'])
def getNotification(notification_id):
    # Fetch notification from database
    notification = db.get_notification(notification_id)

    return json.dumps({'notification': notification}), 200, {'ContentType':'application/json'} 

if __name__ == '__main__':
    app.run(debug=True)
```