from tkinter import *

def interfaceStart():
    win = Tk()
    win.title("test Tkinter")
    win.geometry("300x250")

    label = Label(text="test messeng")
    label.pack()

    win.mainloop()