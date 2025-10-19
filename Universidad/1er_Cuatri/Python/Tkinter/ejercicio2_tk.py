
from tkinter import *

root = Tk()
root.geometry("200x200")
etiqueta1 = Label(text='Etiqueta 1')
etiqueta2 = Label(text='Etiqueta 2')
etiqueta3 = Label(text='Etiqueta 3')
etiqueta4 = Label(text='Etiqueta 4')

'''etiqueta1.pack(padx=10, pady=5)
etiqueta2.pack(padx=10, pady=5)
etiqueta3.pack(padx=10, pady=5)
etiqueta4.pack(padx=10, pady=10)'''

etiqueta1.pack(side=TOP, pady=10)
etiqueta2.pack(side=BOTTOM, pady=10)
etiqueta3.pack(side=LEFT, pady=10)
etiqueta4.pack(side=RIGHT, pady=10)

root.mainloop()