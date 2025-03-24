from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('users.db')  # Connect to your SQLite database
    conn.row_factory = sqlite3.Row  # Allows access to rows by column name
    return conn

# Home route to display the login form
@app.route('/')
def login():
    return render_template('login.html')  # This will load your login.html form from the templates folder

# Route to handle form submission and login authentication
@app.route('/login', methods=['POST'])
def login_user():
    username = request.form['username']
    password = request.form['password']

    # Connect to the database and verify the credentials
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
    conn.close()

    # Check if user exists and credentials match
    if user:
        return redirect(url_for('welcome', username=username))  # Redirect to welcome page on success
    else:
        return "Invalid username or password. Please try again."  # Return error if login fails

# Route to display the welcome page after successful login
@app.route('/welcome/<username>')
def welcome(username):
    return f'Welcome {username}! You have successfully logged in.'  # Display a welcome message

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
