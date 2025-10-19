
from tkinter import *

filas = 3
columnas = 4

root = Tk()

for fila in range(filas):
    root.rowconfigure(fila, weight=1)
    for columna in range(columnas):
        etiqueta = Label(text="etiqueta"+str(fila)+str(columna),bg="red")
        etiqueta.grid(row=fila, column=columna, padx=2, pady=2, sticky="NSEW")
root.mainloop()