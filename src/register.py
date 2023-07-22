```python
from flask import Flask, request, jsonify
from src.database import db, UserSchema
from werkzeug.security import generate_password_hash

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if not username or not password or not email:
        return jsonify({'message': 'Missing data'}), 400

    hashed_password = generate_password_hash(password)

    new_user = UserSchema(username=username, password=hashed_password, email=email)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'register_success', 'user_id': new_user.id}), 201
```