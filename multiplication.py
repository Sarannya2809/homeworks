import tkinter as tk

def multiply():
    n1 = int(e1.get())
    n2 = int(e2.get())
    label_final.config(text=f"Product: {n1 * n2}")

app = tk.Tk()
e1 = tk.Entry(app)
e1.pack()
e2 = tk.Entry(app)
e2.pack()

tk.Button(app, text="Multiply", command=multiply).pack()
label_final = tk.Label(app, text="Product: ")
label_final.pack()

app.mainloop()