import tkinter as tk
import tkmacosx as tkm

root = tk.Tk()
var = tk.IntVar()

r1 = tkm.Radiobutton(root, text = 'Radiobutton1', value = 1,
                     variable = var, indicatoron = 0, padx = 20)
r2 = tkm.Radiobutton(root, text = 'Radiobutton2', value = 2,
                     variable = var, indicatoron = 0, padx = 20)
r3 = tkm.Radiobutton(root, text = 'Radiobutton3', value = 3,
                     variable = var, indicatoron = 0, padx = 20)

r1.pack(pady = 10)
r2.pack(padx = 10)
r3.pack(pady=10)

root.mainloop()
