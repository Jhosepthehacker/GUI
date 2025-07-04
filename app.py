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
def saludar_al_usuario():
    mensaje_de_saludo = messagebox.showinfo(
  title="Saludos",
  message="Hola, Saludos"       
)

ventana = tk.Tk()
ventana.title("Proyecto GUI")
ventana.geometry("400x400")

etiqueta = tk.Label(ventana, text="Hola, Bienvenido(a) al proyecto", bg="blue)
etiqueta.pack(pady=10)

menu_bar = Menu(ventana)
                    
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Salir", command=salir_pregunta)
menu_bar.add_cascade(label="Opción", menu=file_menu)
                    
ventana.config(menu_bar)
ventana.mainloop()
