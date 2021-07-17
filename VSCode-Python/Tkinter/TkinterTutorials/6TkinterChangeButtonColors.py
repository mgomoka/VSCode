from tkinter import *

window = Tk()
window.title("Tkinter")
window.geometry('350x200')

lbl = Label(window, text="Hello")
lbl.grid(column = 0, row = 0)

btn = Button(window, text = "Click Me", bg = "blue", fg = "yellow")
btn.grid(column = 1, row = 0)
print(btn.keys())

window.mainloop()
