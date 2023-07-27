from tkinter import *

root = Tk()

root.title("Ejemplo Checkbuttons")

playa=IntVar()
montana=IntVar()
turismo=IntVar()

def opcionesViaje():
    opcion = ''

    if(playa.get()==1):
        opcion+=" playa"
    
    if(montana.get()==1):
        opcion+=" montaña"
    
    if(turismo.get()==1):
        opcion+=" turismo rural"

    resultado.config(text=opcion)

Label(root, text="Elige destinos", width=50).pack()

Checkbutton(root, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(root, text="Turismo rural", variable=turismo, onvalue=1, offvalue=0, command=opcionesViaje).pack()

resultado = Label(root)
resultado.pack()

root.mainloop()