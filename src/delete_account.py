```python
from flask import Blueprint, request, jsonify
from src.database import db, UserSchema, DogSchema

delete_account = Blueprint('delete_account', __name__)

@delete_account.route('/delete_account', methods=['POST'])
def delete_account():
    user_id = request.json['user_id']
    user = UserSchema.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify(message="account_deleted"), 200
    else:
        return jsonify(message="User not found"), 404

@delete_account.route('/delete_dog_profile', methods=['POST'])
def delete_dog_profile():
    dog_id = request.json['dog_id']
    dog = DogSchema.query.get(dog_id)
    if dog:
        db.session.delete(dog)
        db.session.commit()
        return jsonify(message="Dog profile deleted"), 200
    else:
        return jsonify(message="Dog profile not found"), 404
```