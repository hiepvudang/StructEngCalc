"""
Date: Jan 17
Start the first GUI program to calculate beams
"""

from tkinter import *

root = Tk()
frame = Frame(root)
# frame.pack()

bottomframe = Frame(root)
# bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

root.mainloop()
