"""Aplicacion Hola Mundo"""
import tkinter as tk

root = tk.Tk()
#asigno un nombre a la aplicacion
root.title('Hola mundo')
#Creo la palabra
hola = tk.Label(root,text="Hola Mundo",font=('Arial 16 bold'),bg='brown',fg='#FF0')
#lo Empacamos
hola.pack()
#Hacemos que se ejecute el programa
root.mainloop()