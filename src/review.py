```python
from flask import Blueprint, request
from src.database import db, ReviewSchema

review = Blueprint('review', __name__)

@review.route('/submit_review', methods=['POST'])
def submit_review():
    review_data = request.get_json()
    review_schema = ReviewSchema()
    new_review = review_schema.load(review_data)
    db.session.add(new_review)
    db.session.commit()
    return {'message': 'review_submitted', 'review_id': new_review.id}

@review.route('/get_reviews/<dog_id>', methods=['GET'])
def get_reviews(dog_id):
    reviews = Review.query.filter_by(dog_id=dog_id).all()
    review_schema = ReviewSchema(many=True)
    result = review_schema.dump(reviews)
    return {'message': 'reviews_retrieved', 'reviews': result}
```