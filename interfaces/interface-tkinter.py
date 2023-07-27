from tkinter import *

root = Tk()

root.title("Ventana de prueba")
#raiz.iconbitmap("icono.ico")
root.resizable(0,0)
root.geometry("650x350")
#root.config(bg="blue")

miFrame = Frame()
miFrame.pack()
miFrame.config(bg="red")
miFrame.config(width="450", height="350")

root.mainloop()
