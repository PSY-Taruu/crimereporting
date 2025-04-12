import tkinter as tk  # ✅ You forgot this line before!
from tkinter import messagebox

def start_home():
    def open_report_page():
        root.destroy()
        import report_crime
        report_crime.start_report_form()

    def logout():
        result = messagebox.askyesno("Logout", "Do you want to logout?")
        if result:
            root.destroy()
            import login
            login.start_login()

    global root
    root = tk.Tk()
    root.title("Dashboard")
    root.geometry("350x250")
    root.configure(bg="#ffffff")

    tk.Label(root, text="Welcome to Dashboard", font=("Arial", 16, "bold"), bg="#ffffff").pack(pady=20)

    tk.Button(
        root, text="Report a Crime", font=("Arial", 12),
        bg="#28a745", fg="white", command=open_report_page
    ).pack(pady=10)

    tk.Button(
        root, text="Logout", font=("Arial", 12),
        bg="#dc3545", fg="white", command=logout
    ).pack(pady=10)

    root.mainloop()
