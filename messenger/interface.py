from tkinter import *
import tempfile, base64   #Для конвертации и зашивания иконки

def interfaceStart():
    win = Tk()
    win.title("test Tkinter")
    win.geometry("640x400")
    win.minsize(640, 400)

    # Вопрос открыт, иконка не отображаеться !!! ?
    ICON = base64.b64decode("iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAIAAAD8GO2jAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAgY0hSTQAAeiYAAICEAAD6AAAAgOgAAHUwAADqYAAAOpgAABdwnLpRPAAAAzZJREFUSEuNVs1uEzEQHocDUSUioVIqDiDopSiA1HKjEhfEO3AAweM13s1TVeVChdoeIgopWb75sXd21xsajaIZezyfPb8bNpHkF4iazIFRAauZ113/87tBDjS65KwRAIrULCjTf3WgAOWi2haA0CyYxqzruupsUSsA3FbtyU0EQA/Di7ybAfRgj4ovGBpVNVlf3BtAut27ARhq70bOG503Qa14d32K3Uvjmdzaf1ZyWgq7nBzAdyyINX5xCWCQErC1jvd/xYeruA8CA7EAkPyTrmsA7X0bmBbrw5xbVbvny/ffjggEBmIvmGNp3fHGFoCr+vmnI3pMTGAg3hXgNgZQV1uziEm2wuaUflYvnxBNA02JwEDEYopEq+/tqGUqAaTAVBMFwPMvqtePuAdMQGAgqhsRiaaalMrFLLNGDld2PVb+1oFJrLQAk0CT4AGgoJpFI1jsxiBlqqL6M/YC9LJAHkAfUbylbo02KYsBnoKkivDJfC81UjAQsYgtuUS/efhIbAMQ59oTf9RziQH/5AVz3XIxGO2mbefRItC20ysFAMgLOMi7RBAztiurXg1JFvkESACWOTipQcb/RX1oaRo0TQ/zlq9b5tt+JwDSygt10FScQvjXLLqunn05ZtOgz29Z1Cc6tbIdBei5z1TVOluJYRX3zuqPX48JdLb8gI6ERds1tWKTZxcNSWpYkm8tTRGXvYkzBPb78h0IDETtl1BIOVoA6NdBAjNVPpkqGR0Upt8QgcBAVABuBFYxIwApBq2jfFQMINJl9eIp0SzQjAgMRAlm28cGk9kalE1tH+euqgQ5ATwgAjmAtsqGALrSSdNSPCS1I8En5/XJKyIQGHbR+KeKd/U2AGSRjRGu2Ol13L+sD67qAzAQ82jKyVbMRkuh4bcNN9T07cUtIYY/9fSm2vkdd8DoCFH41JHcZHRfStsAuM+UxqdvErkj+evLdc1yscRslnGnPEWtWlPT0eTykre0YdjgS3Ow0027jmuHn40aqVLNdF1BvqlP7FtGFLQeHbX31jQtjx2N3louKFMhWGATBra0HeV4dB3FHs514EIkiZ+dm+q5/djOJdYZZO6U9SgJ9T8ZSyB3x3LsuAAAAABJRU5ErkJggg==")
    _, ICON_PATH = tempfile.mkstemp()
    with open(ICON_PATH, "wb") as icon_file:
        icon_file.write(ICON)
    icon = PhotoImage(file=ICON_PATH)
    win.iconphoto(False, icon)

    label = Label(text="test messeng")
    label.pack()

    win.mainloop()

if __name__ == '__main__':
    interfaceStart()