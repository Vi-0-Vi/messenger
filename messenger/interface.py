from tkinter import *

def interfaceStart():
    root = Tk()
    root.title("test Tkinter")
    root.geometry("300x250")

    label = Label(text="test messeng")
    label.pack()

    root.mainloop()