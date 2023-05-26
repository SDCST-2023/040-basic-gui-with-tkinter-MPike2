import tkinter as tk 
from tkinter import *

window = tk.Tk()
window.title("Tk")
window.geometry("500x250")

dogphoto = PhotoImage(file="dog.png")
label1=tk.Label(window, text="Client Database")
label2 = tk.Label(window, image=dogphoto)
button1=tk.Button()






label2.grid(row = 1, column = 1)
label1.grid(row=2, column= 2)





window.mainloop()