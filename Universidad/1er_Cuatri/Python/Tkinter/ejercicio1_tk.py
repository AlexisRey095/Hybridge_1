'''import tkinter as tk
root = tk.Tk()
root.title("Prueba Tkinter")
root.geometry("300x200") # Establece un tamaño visible
tk.Label(root, text="¡Funciona!").pack(padx=20, pady=20)
root.mainloop()'''

from tkinter import Tk, Label

root  = Tk()
root.geometry("400x500")
etiqueta = Label(text='Hola')
etiqueta.pack()
root.mainloop()