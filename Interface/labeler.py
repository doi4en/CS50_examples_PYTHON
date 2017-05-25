# метка

from tkinter import *

# создание базового окна
root = Tk()
root.title("Этo я, метка")
root.geometry("200x50")

# внутри окна создается рамка для размещения других элементов
app = Frame(root)
app.grid()

# создание метки внутри рамки
lbl = Label(app, text = "Вот она я!")
lbl.grid()

# старт событийного цикла
root.mainloop()
