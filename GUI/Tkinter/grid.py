import tkinter as tk

root = tk.Tk()
root.title('Aplicacion')
root.geometry('360x240')
root.resizable(False,False)
titulo = tk.Label(root,text="TITULO")
texto = tk.Label(root,text="Esto es un texto")
subtexto = tk.Label(root,text="Mas texto")
titulo.grid(row=1,column=0,sticky='we')
texto.grid(row=2,column=0)
subtexto.grid(columnspan=2)
root.mainloop()