from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Validate login function
def validate_login(username, password):
    conn = sqlite3.connect('crime_reporting.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()
    conn.close()
    return result

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if validate_login(username, password):
            return redirect(url_for('dashboard'))  # Redirect to the dashboard route
        else:
            flash('Invalid username or password.')
            return redirect(url_for('login'))
    return render_template('login.html')


# Dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

@app.route('/report', methods=['GET', 'POST'])
def report_crime():
    if request.method == 'POST':
        crime_type = request.form['crime_type']
        description = request.form['description']
        report_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = sqlite3.connect('crime_reporting.db')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO reports (crime_type, description, report_time)
            VALUES (?, ?, ?)
        """, (crime_type, description, report_time))
        conn.commit()
        conn.close()

        flash('Crime reported successfully!')
        return redirect(url_for('report_crime'))  # Redirect back to same page to clear form

    return render_template('report.html')



@app.route('/view_reports')
def view_reports():
    conn = sqlite3.connect('crime_reporting.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reports")
    all_reports = cursor.fetchall()
    conn.close()
    print("Reports from DB:", all_reports)  # Good for debugging
    return render_template('view_reports.html', reports=all_reports)



# Logout route
@app.route('/logout')
def logout():
    # Clear the session (optional)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
