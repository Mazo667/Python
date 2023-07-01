"""Aplicacion Modificacion ROOT"""
import tkinter as tk

root = tk.Tk()
root.title('Aplicacion')
#Modifico el tamaño en pixeles del root
root.geometry('360x240')
#Asignamos que el root no se pueda modificar
root.resizable(False,False)
#Hacemos que se ejecute el programa
root.mainloop()