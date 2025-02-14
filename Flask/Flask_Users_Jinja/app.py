import json
from flask import Flask, render_template, abort

app = Flask(__name__)

def load_users():
    """Load and return user data from the JSON file."""
    with open('users.json', 'r') as file:
        return json.load(file)

@app.route('/')
def home():
    """Home route that displays a welcome message and links to other pages."""
    return render_template('home.html')

@app.route('/users')
def all_users():
    """Route to display all user data in a nicely formatted HTML page."""
    users = load_users()
    return render_template('users.html', users=users)

@app.route('/user/<int:user_id>')
def user_profile(user_id):
    """Route to display a single user's profile by their ID."""
    users = load_users()
    # Find the user with the matching id
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        abort(404, description="User not found")
    return render_template('user.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
