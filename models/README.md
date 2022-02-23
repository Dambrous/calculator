#ALL ISTRUCTIONS FOR Tkinter LIBRARY IN ###TabExample.py

#Create a window(ROOT)
window = tk.Tk()

#Width and height
window.geometry("600x600")

#Title of window
window.title("Ciao A Tutti")
#Customize the window
window.resizable(False,False)
window.configure(background="orange")

#Widget-Button(To call up functions)
first_button = tk.Button(text="Questa è un calcolatrice", command=first_print)

#To Place It(Geometry)(System of rows and columns)
first_button.grid(row=0,column=0)

if __name__ == "__main__":
    window.mainloop()

#How to display the window
# window.mainloop()

#PADDING=SPAZIATURA
#fg=colore