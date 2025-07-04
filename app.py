import tkinter as tk
from tkinter import messagebox
from tkinter import Menu

ventana = tk.Tk()
ventana.title("Proyecto GUI")
ventana.geometry("400x400")

etiqueta = tk.Label(ventana, text="Hola, Bienvenido(a) al proyecto", bg="blue)
etiqueta.pack(pady=10)

ventana.mainloop()
