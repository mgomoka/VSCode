from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title("Tkinter")
window.geometry('350x200')

txt = scrolledtext.ScrolledText(window, width = 40, height = 10)
txt.grid(column = 0, row = 0)
txt.insert(INSERT, 'Text')

# To Clear The Contents Of A ScrolledText Widget:
# txt.delete(1.0, END) 

window.mainloop()
