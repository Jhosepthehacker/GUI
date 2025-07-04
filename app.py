import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
from sys import exit
from time import sleep

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

preguntar_al_usuario = input("Este programa requiere de interfaz desea continuar: ")

if preguntar_al_usuario == "si" or preguntar_al_usuario == "sí" or preguntar_al_usuario == "si " or preguntar_al_usuario == "sí ":
    ventana = tk.Tk()
    ventana.title("Proyecto GUI")
    ventana.geometry("400x400")

    etiqueta = tk.Label(ventana, text="Hola, Bienvenido(a) al proyecto", bg="blue)
    etiqueta.pack(pady=10)

    boton = tk.Button(ventana, text="Saludos", command=saludar_al_usuario)
    boton.pack(pady=6)
                    
    menu_bar = Menu(ventana)
                    
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Salir", command=salir_pregunta)
    menu_bar.add_cascade(label="Opción", menu=file_menu)
                    
    ventana.config(menu_bar)
    ventana.mainloop()
elif preguntar_al_usuario == "no" or preguntar_al_usuario == "no ":
    print("El programa requiere de interfaz gráfica y si no estás en un entorno gráfico el programa se cierra")
    sleep(1)
    exit()
    
