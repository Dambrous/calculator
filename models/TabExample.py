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


def first_print():
    popoup_text = "Calculator"
    text_output = tk.Label(window, text=popoup_text, fg="red", font=("Helvetica", 16))
    text_output.grid(row=1, column=1)


def second_function():
    popoup_text = "Secondo Messaggio"
    text_output = tk.Label(window, text=popoup_text, fg="green", font=("Helvetica", 16))
    text_output.grid(row=2, column=1, padx=10)


first_button = tk.Button(text="Questa è un calcolatrice", command=first_print)
first_button.grid(row=0, column=0)

first_button = tk.Button(text="Seconda Funzione", command=second_function)
first_button.grid(row=1, column=0, pady=20)

if __name__ == "__main__":
    window.mainloop()
