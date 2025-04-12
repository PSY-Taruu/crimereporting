# home.py
# home.py
import customtkinter as ctk
import report_crime  # Import this module!

def start_home():
    def logout():
        root.destroy()
        import login
        login.start_login()

    def open_report_crime():
        root.destroy()
        report_crime.start_report_crime()  # Call the function from report_crime

    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Home")
    root.geometry("400x300")

    ctk.CTkLabel(root, text="Welcome!", font=("Arial", 18)).pack(pady=20)

    ctk.CTkButton(root, text="Report Crime", command=open_report_crime).pack(pady=10)
    ctk.CTkButton(root, text="Logout", command=logout).pack(pady=10)

    root.mainloop()
