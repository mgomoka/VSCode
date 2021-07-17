from tkinter import *
from tkmacosx import Marquee

text1 = """This text will move from right to left \
if does not fit the window."""
text2 = """Please hover over the text to move it. \
This text will move only if the cursor hovers over \
the text widget."""

window = Tk()
window['bg'] = '#333'

Marquee(window, bg = '#FEE715', fg = '#101820', text = text1).pack(pady = 10)
m = Marquee(window, fg = '#FEE715', bg = '#101820', text = text2)
m.pack(pady = (0,10), padx = 10)
m.stop(True)
m.bind('<Enter>', lambda _: m.play())
m.bind('<Leave>', lambda _: m.stop())

window.mainloop()
