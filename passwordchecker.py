import tkinter as tk

def check_strength():
    password = entry.get()
    if len(password) < 5:
        res = "Weak"
    elif len(password) < 10:
        res = "Medium"
    else:
        res = "Strong"
    label_status.config(text=f"Strength: {res}")

root = tk.Tk()
entry = tk.Entry(root, show="*")
entry.pack()

btn = tk.Button(root, text="Check", command=check_strength)
btn.pack()

label_status = tk.Label(root, text="Strength: ")
label_status.pack()

root.mainloop()