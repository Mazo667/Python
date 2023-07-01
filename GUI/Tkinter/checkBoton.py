import tkinter as tk

root = tk.Tk()
root.title('Aplicacion')
root.geometry('360x240')
root.resizable(False,False)
miBoton = tk.Checkbutton(root,text="Check si comiste la banana")
miBoton.pack()
root.mainloop()