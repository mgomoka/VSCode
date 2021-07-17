from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Tkinter")
window.geometry('350x200')

chk_state = BooleanVar()
chk_state.set(True) # Set Check State

chk = Checkbutton(window, text = 'Choose', var = chk_state)
chk.grid(column = 0, row = 0)

window.mainloop()
