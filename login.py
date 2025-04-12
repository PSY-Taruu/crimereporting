# login.py
import tkinter as tk
from tkinter import messagebox
import sqlite3

def login():
    username = entry_username.get()
    password = entry_password.get()

    conn = sqlite3.connect('crime_reporting.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()

    conn.close()

    if result:
        root.destroy()  # Close the login window
        import home
        home.start_home()  # Open the home page after successful login
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def start_login():
    global root
    root = tk.Tk()  # Create the main window (root)
    root.title("Crime Reporting System - Login")
    root.geometry("300x200")

    tk.Label(root, text="Username").pack(pady=5)
    global entry_username
    entry_username = tk.Entry(root)
    entry_username.pack()

    tk.Label(root, text="Password").pack(pady=5)
    global entry_password
    entry_password = tk.Entry(root, show='*')
    entry_password.pack()

    tk.Button(root, text="Login", command=login).pack(pady=20)

    root.mainloop()  # Keep the login window running

# Run login page directly
if __name__ == "__main__":
    start_login()  # Only start login when running this file directly
