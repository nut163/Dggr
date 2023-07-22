```python
from flask import Flask, request, jsonify
from src.database import Database
from src.user_profile import UserSchema

app = Flask(__name__)
db = Database()

@app.route('/feedback', methods=['POST'])
def submitFeedback():
    user_id = request.json['user_id']
    feedback = request.json['feedback']

    user = db.get_user(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    user_schema = UserSchema()
    if not user_schema.validate(feedback):
        return jsonify({"message": "Invalid feedback data"}), 400

    db.save_feedback(user_id, feedback)
    return jsonify({"message": "feedback_submitted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
```