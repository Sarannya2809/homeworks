import tkinter as tk
from datetime import date

def get_age():
    birth_year = int(e_year.get())
    current_year = date.today().year
    age = current_year - birth_year
    label_age.config(text=f"Present Age: {age}")

root = tk.Tk()
e_year = tk.Entry(root)
e_year.pack()

tk.Button(root, text="Calculate Age", command=get_age).pack()
label_age = tk.Label(root, text="Present Age: ")
label_age.pack()

root.mainloop()