"""Aplicacion Entrada de Texto"""
import tkinter as tk

root = tk.Tk()
root.title('Aplicacion')
root.geometry('360x240')
root.resizable(False,False)
nombre_label = tk.Label(root,text="Cual es tu nombre")
#entrada de datos
nombre = tk.Entry(root)
nombre_label.pack()
nombre.pack()
root.mainloop()