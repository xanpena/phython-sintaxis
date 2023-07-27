from tkinter import *

root=Tk()

genero=IntVar()

def imprimir():

    #print(genero.get())
    if genero.get() == 1:
        etiqueta.config(text="Has seleccionado Masculino")
    else:
        etiqueta.config(text="Has seleccionado Femenino")

Label(root, text="Género:").pack()

Radiobutton(root, text="Masculino", variable=genero, value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=genero, value=2, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()