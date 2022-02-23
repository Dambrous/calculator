"""#release 1.0(TabCalculator)"""
'#TOOLKIT PYTHON TKINTER'

import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

window = tk.Tk()
window.geometry("450x450"), window.resizable(False, False),
window.title("CALCULATOR"), window.configure(background="green")


def somma():
    popoup_text = "Somma"
    text_output = tk.Label(window, text=popoup_text, fg="red", font=("Helvetica", 16))
    text_output.grid(row=0, column=1, padx=10, sticky="w")


def differenza():
    popoup_text = "Differenza"
    text_output = tk.Label(window, text=popoup_text, fg="green", font=("Helvetica", 16))
    text_output.grid(row=1, column=1, padx=10, sticky="w")


first_button = tk.Button(text="Somma", command=somma)
first_button.grid(row=0, column=0, sticky="w")

first_button = tk.Button(text="Differenza", command=differenza)
first_button.grid(row=1, column=0, pady=20, sticky="w")

if __name__ == "__main__":
    window.mainloop()
