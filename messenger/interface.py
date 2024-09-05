from tkinter import *
from tkinter import ttk
import tempfile, base64, zlib   #Для конвертации и зашивания иконки

clicks = 0

def main_win_interface_start():
    win = Tk()
    win.title("test Tkinter")
    win.geometry("640x400")
    win.resizable(False, False)
    #win.minsize(640, 400)

    # Вопрос открыт, картинка на иконке не отображаеться, но работает в lable !!! ?
    ICON = zlib.decompress(base64.b64decode("eJwBuANH/IlQTkcNChoKAAAADUlIRFIAAAAgAAAAIAgCAAAA/BjtowAAAAFzUkdCAK7OHOkAAAAEZ0FNQQAAsY8L/GEFAAAAIGNIUk0AAHomAACAhAAA+gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAAM2SURBVEhLjVbNbhMxEB6HA1ElIqFSKg4g6KUogNRyoxIXxDtwAMHjNd7NU1XlQoXaHiIKKVm++bF3dtcbGo2iGXs8nz2/GzaR5BeImsyBUQGrmddd//O7QQ40uuSsEQCK1Cwo0391oADlotoWgNAsmMas67rqbFErANxW7clNBEAPw4u8mwH0YI+KLxgaVTVZX9wbQLrduwEYau9GzhudN0GteHd9it1L45nc2n9WcloKu5wcwHcsiDV+cQlgkBKwtY73f8WHq7gPAgOxAJD8k65rAO19G5gW68OcW1W758v3344IBAZiL5hjad3xxhaAq/r5pyN6TExgIN4V4DYGUFdbs4hJtsLmlH5WL58QTQNNicBAxGKKRKvv7ahlKgGkwFQTBcDzL6rXj7gHTEBgIKobEYmmmpTKxSyzRg5Xdj1W/taBSay0AJNAk+ABoKCaRSNY7MYgZaqi+jP2AvSyQB5AH1G8pW6NNimLAZ6CpIrwyXwvNVIwELGILblEv3n4SGwDEOfaE3/Uc4kB/+QFc91yMRjtpm3n0SLQttMrBQDICzjIu0QQM7Yrq14NSRb5BEgAljk4qUHG/0V9aGkaNE0P85avW+bbficA0soLddBUnEL41yy6rp59OWbToM9vWdQnOrWyHQXouc9U1TpbiWEV987qj1+PCXS2/ICOhEXbNbVik2cXDUlqWJJvLU0Rl72JMwT2+/IdCAxE7ZdQSDlaAOjXQQIzVT6ZKhkdFKbfEIHAQFQAbgRWMSMAKQato3xUDCDSZfXiKdEs0IwIDEQJZtvHBpPZGpRNbR/nrqoEOQE8IAI5gLbKhgC60knTUjwktSPBJ+f1ySsiEBh20fininf1NgBkkY0Rrtjpddy/rA+u6gMwEPNoyslWzEZLoeG3DTfU9O3FLSGGP/X0ptr5HXfA6AhR+NSR3GR0X0rbALjPlManbxK5I/nry3XNcrHEbJZxpzxFrVpT09Hk8pK3tGHY4EtzsNNNu45rh5+NGqlSzXRdQb6pT+xbRhS0Hh2199Y0LY8djd5aLihTIVhgEwa2tB3leHQdxR7OdeBCJImfnZvquf3YziXWGWTulPUoCfU/GUsgd8dy7LgAAAAASUVORK5CYIJZ+qOp"))
    _, ICON_PATH = tempfile.mkstemp()
    with open(ICON_PATH, "wb") as icon_file:
        icon_file.write(ICON)
    icon = PhotoImage(file=ICON_PATH)
    win.iconphoto(False, icon)

    label = Label(text="test messeng")
    label.pack(expand=True, fill=BOTH)

    def click_button():
        global clicks
        clicks += 1
        # изменяем текст на кнопке
        label["text"] = f"Clicks {clicks}"
    def entered(event):
        btn["text"] = "Entered"
    def left(event):
        btn["text"] = "Left"
    def single_click(event):
        btn["text"] = "Single Click"
    def double_click(event):
        btn["text"] = "Double Click"
    btn = ttk.Button(text="Button", command=click_button)
    btn.pack(anchor=SE, padx=5, pady=5)
    btn.bind("<Enter>", entered)
    btn.bind("<Leave>", left)
    btn.bind("<ButtonPress-1>", single_click)
    btn.bind("<Double-ButtonPress-1>", double_click)

    win.mainloop()

def main():
    main_win_interface_start()

if __name__ == '__main__':
    main()