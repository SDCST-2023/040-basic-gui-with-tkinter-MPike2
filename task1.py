import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("Tk")
window.geometry("430x60")
a=tk.Entry(window, width=10)
a.pack(side=LEFT)
x=tk.Label(text="x")
x.pack(side=LEFT)
b=tk.Entry(window, width=10)
b.pack(side=LEFT)
z=tk.Label(text="=")
z.pack(side=LEFT)
c=tk.Entry(window, width=25)
c.pack(side=LEFT)

window.mainloop()
