import tkinter as tk

def test_ui():
    root = tk.Tk()
    root.title("Style Test")
    root.geometry("400x300")
    root.configure(bg="#f5f6fa")

    label = tk.Label(root, text="Styled Label", font=("Arial", 16, "bold"), fg="blue", bg="#f5f6fa")
    label.pack(pady=20)

    entry = tk.Entry(root, font=("Arial", 12), bg="white", fg="black")
    entry.pack(pady=10)

    btn = tk.Button(root, text="Styled Button", font=("Arial", 12, "bold"), bg="#0984e3", fg="white")
    btn.pack(pady=20)

    root.mainloop()

test_ui()
