```python
from flask import Flask, request, jsonify
from src.database import db, UserSchema, SubscriptionSchema

app = Flask(__name__)

@app.route('/subscription', methods=['POST'])
def update_subscription():
    user_id = request.json['user_id']
    subscription_id = request.json['subscription_id']
    user = UserSchema.query.get(user_id)
    subscription = SubscriptionSchema.query.get(subscription_id)

    if not user or not subscription:
        return jsonify({'message': 'User or subscription not found'}), 404

    user.subscription_id = subscription_id
    db.session.commit()

    return jsonify({'message': 'subscription_updated', 'subscription_id': subscription_id}), 200

@app.route('/subscription', methods=['GET'])
def get_subscription():
    user_id = request.args.get('user_id')
    user = UserSchema.query.get(user_id)

    if not user:
        return jsonify({'message': 'User not found'}), 404

    subscription = SubscriptionSchema.query.get(user.subscription_id)

    return jsonify({'subscription_id': subscription.subscription_id, 'subscription_type': subscription.subscription_type}), 200
```