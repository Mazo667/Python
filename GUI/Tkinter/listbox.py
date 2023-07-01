import tkinter as tk

root = tk.Tk()
root.title('Aplicacion')
root.geometry('360x240')
root.resizable(False,False)
nombre_label = tk.Label(root,text="Cual es tu color favorito")
color = tk.Listbox(root,height=4) 
colores = ['Rojo','Verde','Negro','Celeste']
for miColor in colores:
    color.insert(tk.END,miColor)
nombre_label.pack()
color.pack()
root.mainloop()