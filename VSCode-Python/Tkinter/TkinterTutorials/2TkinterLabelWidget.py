from tkinter import *

window = Tk()
window.title("Tkinter")

lbl = Label(window, text = "Hello")
lbl.grid(column = 0, row = 0)

window.mainloop()
