```python
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

THEME_DIRECTORY = os.path.join(os.getcwd(), 'assets', 'themes')

def get_all_themes():
    themes = os.listdir(THEME_DIRECTORY)
    return themes

@app.route('/theme', methods=['GET'])
def get_theme():
    user_id = request.args.get('user_id')
    # Fetch user's current theme from database
    # This is a placeholder and should be replaced with actual database call
    user_theme = "default"
    return jsonify({"theme": user_theme}), 200

@app.route('/theme', methods=['POST'])
def change_theme():
    user_id = request.args.get('user_id')
    new_theme = request.json.get('theme')
    if new_theme not in get_all_themes():
        return jsonify({"error": "Theme not found"}), 404
    # Update user's theme in database
    # This is a placeholder and should be replaced with actual database call
    return jsonify({"message": "Theme changed successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
```