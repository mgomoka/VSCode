from tkinter import *
from tkmacosx import Button

window = Tk()
window.geometry('200x150')

B0 = Button(window, text = 'Button0')
B0.pack(padx = 20, pady = (20, 0))
B1 = Button(window, text = 'Button', bg = '#ADEFD1', fg = '#00203F', borderless = 1)
B1.pack(padx = 20, pady = 10)
B2 = Button(window, text = 'Button', bg = '#E69A8D', fg = '#5F4B8B', borderless = 1,
            activebackground = ('#AE0E36', '#D32E5E'), activeforeground = '#E69A8D')
B2.pack()

window.mainloop()
