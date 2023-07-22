```python
from flask import Flask, request, jsonify
from src.database import db, UserSchema

app = Flask(__name__)

@app.route('/user_profile', methods=['GET', 'POST', 'PUT'])
def user_profile():
    if request.method == 'GET':
        user_id = request.args.get('user_id')
        user = db.get_user(user_id)
        return jsonify(UserSchema().dump(user))

    elif request.method == 'POST':
        user_data = request.get_json()
        new_user = UserSchema().load(user_data)
        db.add_user(new_user)
        return jsonify(message='User profile created successfully'), 201

    elif request.method == 'PUT':
        user_id = request.args.get('user_id')
        user_data = request.get_json()
        updated_user = UserSchema().load(user_data)
        db.update_user(user_id, updated_user)
        return jsonify(message='User profile updated successfully')

@app.route('/user_profile/delete', methods=['DELETE'])
def delete_user_profile():
    user_id = request.args.get('user_id')
    db.delete_user(user_id)
    return jsonify(message='User profile deleted successfully')

if __name__ == '__main__':
    app.run(debug=True)
```