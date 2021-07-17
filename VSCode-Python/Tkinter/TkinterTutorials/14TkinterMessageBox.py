from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tkinter")
window.geometry('350x200')

def clicked():
    messagebox.showinfo('Message Title', 'Message Content')
    #messagebox.showwarning('Message Title', 'Message Content')
    #messagebox.showerror('Message Title', 'Message Content')
btn = Button(window, text = 'Click Here', command = clicked)
btn.grid(column = 0, row = 0)

window.mainloop()
