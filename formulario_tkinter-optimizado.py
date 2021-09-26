from tkinter import *

class label_input ():
  def __init__ (self, parent, labeltext="", typeinput="str"):
    self.label = Label(parent, text=labeltext)

    if typeinput == "str":
      self.input = StringVar()
    elif typeinput == "int":
      self.input = IntVar()

    self.entry = Entry(parent, textvariable=self.input)

  def show_data (self, initial_row=0, initial_column=0, span=1):
    self.label.grid(row=initial_row, column=initial_column, columnspan=span)
    initial_column += span
    self.entry.grid(row=initial_row, column=initial_column, columnspan=span)

def datos_ingresados ():
  nombre = name.input.get()
  apellido = lastName.input.get()
  edad = age.input.get()

  datos = Label(base)
  datos["text"] = f"Hola. Bienvenido {nombre} {apellido}, tienes {edad} años"

  datos.grid(row=5, column=0, columnspan=3, sticky=W)

base = Tk()

main_label = Label(base, text="Ingresa tus Datos:  ")
name = label_input(base, labeltext="Nombre: ")
lastName = label_input(base, labeltext="Apellido: ")
age = label_input(base, labeltext="Edad: ", typeinput="int")
start_button = Button(base, width=50, text="Ingresar Datos", command=datos_ingresados)

# Join / Show
main_label.grid(row=0, column=0)
name.show_data(1, 1)
lastName.show_data(2, 1)
age.show_data(3, 1)
start_button.grid(row=4, column=0, columnspan=3)

base.mainloop()