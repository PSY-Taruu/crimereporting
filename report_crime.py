import tkinter as tk
from tkinter import messagebox
import sqlite3

def submit_report():
    crime_type = entry_type.get()
    description = text_description.get("1.0", tk.END).strip()

    if not crime_type or not description:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    try:
        conn = sqlite3.connect('crime_reporting.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reports (crime_type, description) VALUES (?, ?)", (crime_type, description))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Crime report submitted successfully!")
        entry_type.delete(0, tk.END)
        text_description.delete("1.0", tk.END)
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")

def start_report_page():
    global entry_type, text_description

    window = tk.Tk()
    window.title("Crime Report")
    window.geometry("500x500")
    window.configure(bg="#f5f6fa")  # Light background

    # Title
    title = tk.Label(window, text="Report a Crime", font=("Arial", 20, "bold"), bg="#f5f6fa", fg="#2f3640")
    title.pack(pady=20)

    # Crime Type Label
    lbl_type = tk.Label(window, text="Crime Type", font=("Arial", 12), bg="#f5f6fa", anchor="w")
    lbl_type.pack(padx=20, fill="x")
    entry_type = tk.Entry(window, font=("Arial", 12), width=40)
    entry_type.pack(pady=5)

    # Description Label
    lbl_desc = tk.Label(window, text="Description", font=("Arial", 12), bg="#f5f6fa", anchor="w")
    lbl_desc.pack(padx=20, fill="x", pady=(15, 0))
    text_description = tk.Text(window, height=8, width=50, font=("Arial", 12))
    text_description.pack(pady=5)

    # Submit Button
    btn_submit = tk.Button(
        window, text="Submit", font=("Arial", 12, "bold"),
        bg="#0984e3", fg="white", activebackground="#74b9ff",
        command=submit_report
    )
    btn_submit.pack(pady=30)

    window.mainloop()
