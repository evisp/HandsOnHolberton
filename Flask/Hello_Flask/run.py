from flask import Flask

app = Flask(__name__)

# 1. Route that returns a simple "Hello Flask!" message.
@app.route('/')
def hello_flask():
    return "Hello Flask!"

# 2. Route that takes a user's name as part of the URL and greets them.
#    For example, going to '/greet/Alice' will display "Hello, Alice! Welcome to our Flask app."
@app.route('/greet/<name>')
def greet_user(name):
    return f"Hello, {name}! Welcome to our Flask app."

# 3. Route that takes a user ID (as an integer) and displays a message related to that ID.
#    For example, going to '/user/123' will display "This is the profile page for user with ID: 123."
@app.route('/user/<int:user_id>')
def user_profile(user_id):
    return f"is the profile page for user with ID: {user_id}."

# Run the Flask app and test the routes in the browser.
# Go to http://localhost:5000/ to see the "Hello Flask!" message.
if __name__ == '__main__':
    app.run(debug=True)
