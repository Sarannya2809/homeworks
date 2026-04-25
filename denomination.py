import tkinter as tk

def calculate():
    amount = int(entry.get())
    notes = [2000, 500, 200, 100, 50, 20, 10]
    res = ""
    for note in notes:
        count = amount // note
        amount %= note
        res += f"{note}s: {count}\n"
    label_res.config(text=res)

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Calculate Notes", command=calculate).pack()
label_res = tk.Label(root, text="")
label_res.pack()

root.mainloop()