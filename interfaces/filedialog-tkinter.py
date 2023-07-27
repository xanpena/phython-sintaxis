from tkinter import *
from tkinter import filedialog

root=Tk()

def abreFichero():

    fichero=filedialog.askopenfilename(title="Abrir", initialdir="c:", filetypes=(('Ficheros de Excel', '*.xlsx'), ('Ficheros de texto', '*.txt'))) # Devuelve la ruta

    print(fichero)

Button(root, text="Abrir fichero", command=abreFichero).pack()

root.mainloop()