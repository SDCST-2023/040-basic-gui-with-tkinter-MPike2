import tkinter as tk 
from tkinter import *



window = tk.Tk()
window.title("Tk")
window.geometry("300x200")

img1=PhotoImage(file="dog.png")

Img1=tk.Label(window, image=img1)


Img1.place(x=75, y=20)

d1=tk.Label(text="Pocchacco")
d1.place(x=150, y=50)

nF = Frame()
f2 = Label(nF,text="another widget!", background="#aaffff")
f2.place(x=150, y = 150)

window.mainloop()