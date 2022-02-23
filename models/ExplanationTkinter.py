#release 1.0
#TOOLKIT PYTHON TKINDER

#import tkinter as tk(Doesnt Work without the following function)

import sys
if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

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
first_button = tk.Button(text="Questa è un calcolatrice")

#To Place It(Geometry)(System of rows and columns)
first_button.grid(row=0,column=0)

if __name__ == "__main__":
    window.mainloop()

#How to display the window
# window.mainloop()