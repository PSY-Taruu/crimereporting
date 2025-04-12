# db_setup.py
import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect('crime_reporting.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Optional: Add a test user
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ("admin", "admin123"))

conn.commit()
conn.close()

