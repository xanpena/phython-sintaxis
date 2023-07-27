from tkinter import *
from tkinter import messagebox

root=Tk()

def acercaDe():
    messagebox.showinfo("Mi editor", "Versión: 0.0.1")

def salir():
    valor = messagebox.askokcancel("Cerrar aplicación", "¿Seguro que quieres cerrar la aplicación?")

    if valor == True:
        root.destroy()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=450, height=350)

menu_archivo=Menu(barraMenu, tearoff=0)
menu_archivo.add_command(label="Nuevo")
menu_archivo.add_command(label="Abrir")
menu_archivo.add_command(label="Guardar")
menu_archivo.add_command(label="Guardar como")
menu_archivo.add_separator()
menu_archivo.add_command(label="Cerrar")
menu_archivo.add_command(label="Salir", command=salir)

menu_edicion=Menu(barraMenu, tearoff=0)
menu_edicion.add_command(label="Deshacer")
menu_edicion.add_command(label="Rehacer")

menu_tools=Menu(barraMenu, tearoff=0)
menu_tools.add_command(label="Python")

menu_help=Menu(barraMenu, tearoff=0)
menu_help.add_command(label="Acerca de", command=acercaDe)


barraMenu.add_cascade(label="Archivo", menu=menu_archivo)
barraMenu.add_cascade(label="Edición", menu=menu_edicion)
barraMenu.add_cascade(label="Herramientas", menu=menu_tools)
barraMenu.add_cascade(label="Ayuda", menu=menu_help)

root.mainloop()