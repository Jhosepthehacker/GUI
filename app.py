import tkinter as tk
from tkinter import messagebox
from tkinter import Menu

def salir_pregunta():
    mensaje_de_pregunta = messagebox.askquestion(
   title="Pregunta",
   message="¿Quiéres salir de la ventana?"   
)
    if (mensaje_de_pregunta == "yes"):
        print("Ventana cerrada")
        ventana.destroy()
    else:
        print("La ventana todavía sigue abierta")
      
ventana = tk.Tk()
ventana.title("Proyecto GUI")
ventana.geometry("400x400")

etiqueta = tk.Label(ventana, text="Hola, Bienvenido(a) al proyecto", bg="blue)
etiqueta.pack(pady=10)

try:
    ventana.config(menu_bar) # En desarrollo hasta que se creé la barra de menú y opciones
except NameError:
    print("Se capturó un NameError")
ventana.mainloop()
