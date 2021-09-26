from tkinter import *

base = Tk()
screen_height = int(base.winfo_screenheight() / 4)
screen_width = int(base.winfo_screenwidth() / 4)

base["bg"] = "#f5f5f5"
base["width"] = screen_width

def datos_ingresados ():
  nombre = input_name.get()
  apellido = input_lastName.get()
  edad = input_edad.get()

  datos = Label(base)
  datos["text"] = f"Hola. Bienvenido {nombre} {apellido}, tienes {edad} años"

  datos.grid(row=5, column=0, columnspan=3, sticky=W)

# Inputs Values
input_name = StringVar()
input_lastName = StringVar()
input_edad = IntVar()

# Labels
main_label = Label(base, text="Ingresa tus Datos:  ")
label_name = Label(base, text="Nombre: ")
label_lastName = Label(base, text="Apellido: ")
label_edad = Label(base, text="Edad:")

# Inputs Entries
entry_name = Entry(base, width=50, textvariable=input_name)
entry_lastName = Entry(base, width=50, textvariable=input_lastName)
entry_edad = Entry(base, width=50, textvariable=input_edad)

start_button = Button(base, width=50, text="Ingresar Datos", command=datos_ingresados)

# Join / Show
main_label.grid(row=0, column=0)
label_name.grid(row=1, column=1)
entry_name.grid(row=1, column=2)
label_lastName.grid(row=2, column=1)
entry_lastName.grid(row=2, column=2)
label_edad.grid(row=3, column=1)
entry_edad.grid(row=3, column=2)
start_button.grid(row=4, column=0, columnspan=3)

base.mainloop()