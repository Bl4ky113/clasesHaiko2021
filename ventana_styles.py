from tkinter import *

base = Tk()
base["bg"] = "#aaffdd"

def mensaje_function ():
  mensaje.configure(text="Hola Tkinter")
  mensaje.grid(row=0, column=0) 

mensaje = Label(base, fg="#006600", font=("Georgia", 14))
boton_death = Button(base, text="Kill", command=mensaje_function)

boton_death.grid(row=0, column=1)

base.mainloop()