```python
from flask import Flask, request, jsonify
from src.database import get_db

app = Flask(__name__)

@app.route('/help_support', methods=['POST'])
def requestHelp():
    user_id = request.form['user_id']
    help_request = request.form['help_request']

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'INSERT INTO help_support (user_id, help_request) VALUES (?, ?)',
        (user_id, help_request)
    )
    db.commit()

    return jsonify({'message': 'help_requested'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```