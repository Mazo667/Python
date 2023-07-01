import tkinter as tk

root = tk.Tk()
root.title('Aplicacion')
root.geometry('360x240')
root.resizable(False,False)
nombre_label = tk.Label(root,text="Cuantas bananas comiste?")
num = tk.Spinbox(root,from_=0,to=100,increment=1)
nombre_label.pack()
num.pack()
root.mainloop()