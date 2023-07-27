from tkinter import *

root = Tk()

miFrame=Frame(root, width=1200, height=600)
miFrame.pack()

minombre=StringVar()

inputTexto=Entry(miFrame, textvariable=minombre)
inputTexto.grid(row=0, column=1)

inputPass=Entry(miFrame)
inputPass.grid(row=1, column=1)

textComentario=Text(miFrame, width=16, height=5)
textComentario.grid(row=2, column=1, pady=5)

scrollY=Scrollbar(miFrame, command=textComentario.yview)
scrollY.grid(row=2, column=2, sticky="nsew")

textComentario.config(yscrollcommand=scrollY.set)


labelNombre=Label(miFrame, text="Nombre:")
labelNombre.grid(row=0, column=0, sticky="e", pady=5)

labelPass=Label(miFrame, text="Password:", pady=5)
labelPass.grid(row=1, column=0)

labelComentario=Label(miFrame, text="Comentario:", pady=5)
labelComentario.grid(row=2, column=0, sticky="n")

def codigoBoton():
    minombre.set("Xan")

buttonEnvio=Button(root, text="Enviar", command=codigoBoton)
buttonEnvio.pack()

root.mainloop()