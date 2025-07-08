import tkinter as tk
from tkinter import messagebox
from tkinter import Menu
from sys import exit
from time import sleep

def salir_pregunta():
    message_of_question = messagebox.askquestion(
   title="Pregunta",
   message="¿Quiéres salir de la ventana?"   
)
    if (message_of_question == "yes"):
        print("Ventana cerrada")
        root.destroy()
    else:
        print("La ventana todavía sigue abierta")
def saludar_al_usuario():
    mensaje_de_saludo = messagebox.showinfo(
  title="Saludos",
  message="Hola, Saludos"       
)

question_to_user = input("Este programa requiere de interfaz desea continuar, ¿Estás en un entorno gráfico?: ")

if question_to_user == "si" or question_to_user == "sí" or question_to_user == "si " or question_to_user == "sí ":
    root = tk.Tk()
    root.title("Proyecto GUI")
    root.geometry("400x400")

    label = tk.Label(root, text="Hola, Bienvenido(a) al proyecto", bg="blue")
    label.pack(pady=10)

    button = tk.Button(root, text="Saludos", command=saludar_al_usuario)
    button.pack(pady=6)
                    
    menu_bar = Menu(root)
                    
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Salir", command=salir_pregunta)
    menu_bar.add_cascade(label="Opción", menu=file_menu)

    try:
        root.config(menu_bar) # TypeError, en desarrollo....
    except TypeError:
        print("Hubo un TypeError, el menú de opciones no se mostrará")
    root.mainloop()
elif question_to_user == "no" or question_to_user == "no ":
    print("\nEl programa requiere de interfaz gráfica y si no estás en un entorno gráfico el programa se cierra")
    sleep(4)
    exit()
