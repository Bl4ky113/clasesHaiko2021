from tkinter import *

base = Tk()

mensaje = Label(base, text="Hello Tkinter")
boton_death = Button(base, text="Kill", command=base.destroy)

mensaje.grid(row=0, column=0) 
boton_death.grid(row=0, column=1)

base.mainloop()