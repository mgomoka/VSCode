from tkinter import *

window = Tk()
window.geometry('200x150')

width = window.winfo_screenwidth()       
height = window.winfo_screenheight()         
window.geometry("%dx%d" % (width, height))

window.mainloop()
