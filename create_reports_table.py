import sqlite3

# Connect to your existing database
conn = sqlite3.connect('crime_reporting.db')
cursor = conn.cursor()

# Create the 'reports' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    crime_type TEXT NOT NULL,
    description TEXT NOT NULL,
    report_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
''')

conn.commit()
conn.close()

print("✅ 'reports' table created successfully (if it didn’t exist already).")
