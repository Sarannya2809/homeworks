import tkinter as tk

def convert():
    inches = float(entry.get())
    cm = inches * 2.54
    label_result.config(text=f"Centimeters: {cm}")

window = tk.Tk()
window.title("Length Converter")

entry = tk.Entry(window)
entry.pack()

btn = tk.Button(window, text="Convert", command=convert)
btn.pack()

label_result = tk.Label(window, text="Centimeters: 0")
label_result.pack()

window.mainloop()