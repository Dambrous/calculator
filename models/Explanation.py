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

#How to display the window
window.mainloop()
