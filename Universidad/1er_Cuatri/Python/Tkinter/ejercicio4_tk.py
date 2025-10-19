from tkinter import *
from tkinter import ttk # Importar ttk

root = Tk()
root.geometry("200x200")

# --- Solución: Usar estilos de ttk para forzar los colores ---

# 1. Configurar el estilo "clam" que permite personalización
style = ttk.Style()
style.theme_use("clam")

# 2. Definir un estilo personalizado para el botón
style.configure("MiEstilo.TButton",
                background="green",
                foreground="white", # Color del texto normal
                relief=RAISED)

# 3. Definir cómo se ve el estilo cuando está "activo" (hover)
style.map("MiEstilo.TButton",
          background=[('active', 'blue')])

# Crear el botón usando ttk.Button y nuestro estilo
# ttk.Button no usa los argumentos 'background' o 'activebackground' directamente
# sino que usa el argumento 'style'
button = ttk.Button(
    root,
    text="Haz clic (con ttk)",
    style="MiEstilo.TButton",
    command=lambda: print("Clic exitoso")
)

# La etiqueta sigue funcionando con bg normal, activebackground se ignora aquí
etiqueta = Label(text='Etiqueta', bg="blue", activebackground="green")
etiqueta.pack(padx=10, pady=10, ipadx=10, ipady=10)

button.pack(pady=20)
root.mainloop()


