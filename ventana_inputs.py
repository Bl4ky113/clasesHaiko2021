from tkinter import *

base = Tk()
base["bg"] = "#aaffdd"

def mensaje_function ():
  mensaje["text"] = tk_input.get()
  mensaje.grid(row=1, column=0, columnspan=4) 

valor_input = StringVar()

tk_input = Entry(base, width=20, justify=CENTER, textvariable=valor_input)
mensaje = Label(base, fg="#006600", font=("Georgia", 14))
boton_death = Button(base, text="Show Text", command=mensaje_function)

tk_input.grid(row=0, column=0, columnspan=4)
boton_death.grid(row=2, column=0, columnspan=4)

base.mainloop()