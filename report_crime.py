# report_crime.py
# report_crime.py
import customtkinter as ctk
import sqlite3
from tkinter import messagebox

def start_report_crime():
    def submit_report():
        crime_type = entry_crime_type.get()
        description = entry_description.get()

        conn = sqlite3.connect('crime_reporting.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reports (crime_type, description) VALUES (?, ?)", (crime_type, description))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Crime reported successfully!")
        root.destroy()

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Report Crime")
    root.geometry("400x300")

    ctk.CTkLabel(root, text="Crime Type:").pack(pady=5)
    entry_crime_type = ctk.CTkEntry(root)
    entry_crime_type.pack(pady=5)

    ctk.CTkLabel(root, text="Description:").pack(pady=5)
    entry_description = ctk.CTkEntry(root)
    entry_description.pack(pady=5)

    ctk.CTkButton(root, text="Submit", command=submit_report).pack(pady=20)

    root.mainloop()

