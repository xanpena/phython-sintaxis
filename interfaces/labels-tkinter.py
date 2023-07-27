from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

miLabel = Label(miFrame, text="Hola Python :)", fg="blue", font=("Arial bold", 14))
miLabel.place(x=100, y=200)

# miImagen=PhotoImage(file="mouse.gif")
# Label(miFrame, image=miImagen).place(x=100, y=200)

root.mainloop()