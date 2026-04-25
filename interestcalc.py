import tkinter as tk

def calculate():
    p = float(entry_p.get())
    t = float(entry_t.get())
    r = float(entry_r.get())
    si = (p * t * r) / 100
    label_res.config(text=f"Simple Interest: {si}")

root = tk.Tk()
entry_p = tk.Entry(root)
entry_p.pack()
entry_t = tk.Entry(root)
entry_t.pack()
entry_r = tk.Entry(root)
entry_r.pack()

tk.Button(root, text="Calculate", command=calculate).pack()
label_res = tk.Label(root, text="Simple Interest: ")
label_res.pack()

root.mainloop()