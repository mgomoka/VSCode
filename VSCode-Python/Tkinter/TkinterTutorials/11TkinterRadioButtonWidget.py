from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Tkinter")
window.geometry('350x200')

rad1 = Radiobutton(window, text = 'First', value = 1)
rad2 = Radiobutton(window, text = 'Second', value = 2)
rad3 = Radiobutton(window, text = 'Third', value = 3)
# Note that you should set the value for every radio button with a 
# different value, otherwise, they won’t work.

rad1.grid(column = 0, row = 0)
rad2.grid(column = 1, row = 0)
rad3.grid(column = 2, row = 0)

def clicked():
    pass
rad4 = Radiobutton(window,text = 'Click', value = 1, command = clicked)
rad4.grid(column = 3, row = 0)

window.mainloop()
