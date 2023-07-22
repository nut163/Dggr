```python
import stripe
from src.database import UserSchema, SubscriptionSchema

stripe.api_key = "your_stripe_api_key"

def makePayment(user_id, subscription_id):
    user = UserSchema.query.get(user_id)
    subscription = SubscriptionSchema.query.get(subscription_id)

    if not user or not subscription:
        return {"message": "User or Subscription not found"}, 404

    try:
        charge = stripe.Charge.create(
            amount=subscription.price * 100,  # Stripe requires the amount in cents
            currency="usd",
            customer=user.stripe_customer_id,
            description=f"Payment for {subscription.name}",
        )

        if charge.paid:
            user.subscription_id = subscription_id
            user.save_to_db()
            return {"message": "payment_made"}, 200
        else:
            return {"message": "Payment failed"}, 400

    except Exception as e:
        return {"message": str(e)}, 500
```