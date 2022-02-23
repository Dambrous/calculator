import tkinter as tk
import requests

window = tk.Tk()
window.geometry("900x550")
window.title("ASCII ART DOWNLOADER")
window.grid_columnconfigure(0, weight=1)


"""#FUNCTIONS"""


def download_ascii():
    if text_input.get():
        user_input = text_input.get()
        payload = {"text": user_input}
        response = requests.get("http://artii.herokuapp.com/make",
                                params=payload)
        text_response = response.text
    else:
        text_response = "Aggiungi una parola o una frase al campo input!"

    textwidget = tk.Text()
    textwidget.insert(tk.END, text_response)
    textwidget.grid(row=3, column=0, sticky="We", padx=10)


welcome_label = tk.Label(window,
                         text="Welcome! Aggiungi una parola o una frase da scaricare:",
                         pady=10, font=("Helvetica", 15))
welcome_label.grid(row=0, column=0, sticky="N", pady=10)

text_input = tk.Entry()
text_input.grid(row=1, column=0, sticky="WE", padx=25)

download_button = tk.Button(text="DOWNLOAD ASCII ART", command=download_ascii)
download_button.grid(row=2, column=0, sticky="WE", padx=25, pady=25)

if __name__ == "__main__":
    window.mainloop()
