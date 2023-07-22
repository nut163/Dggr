```python
from flask import Flask, session, redirect, url_for
from src.database import get_db

app = Flask(__name__)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('dog_id', None)
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
```