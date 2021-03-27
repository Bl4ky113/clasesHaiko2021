# Clases 
class persona:
  def __init__ (self, nombre, edad, estatura, fruta_fav):
    self.nombre = nombre
    self.edad = edad
    self.estatura = estatura 
    self.fruta_fav = fruta_fav 

Juan = persona("Juan", 34, 1.53, "Mango")
Pedro = persona("Pedro", 19, 1.68, "Manzana")
Pepito = persona("Pepito", 37, 1.76, "Pera")

print(Juan.nombre)