from tkinter import *
from tkmacosx import Button
import sys

window = Tk()
window.title('Lemonade')
window['bg'] = 'salmon'
window.attributes('-alpha', 0.8)
screenWidth = int(window.winfo_screenwidth())
screenHeight = int(window.winfo_screenheight())
windowWidth = int((screenWidth/8)*7)
windowHeight = int((screenHeight/8)*7)
centerX = int(screenWidth/2 - windowWidth/2)
centerY = int(screenHeight/2 - windowHeight/2)
window.geometry(f'{windowWidth}x{windowHeight}+{centerX}+{centerY-30}')

canvas = Canvas(window, bg = 'salmon', confine = True, 
                width = windowWidth-100, height = windowHeight-100)

# canvas.place(relx = 0.5, rely = 0.5, anchor = CENTER)
canvas.pack(expand = YES, fill = BOTH)
window.mainloop()
