import tkinter as tk

root = tk.Tk()
root.title('Aplicacion')
root.geometry('360x240')
root.resizable(False,False)
label = tk.Label(root,text="Escribe algo")
texto = tk.Text(root,height=5)
label.pack()
texto.pack()
root.mainloop()