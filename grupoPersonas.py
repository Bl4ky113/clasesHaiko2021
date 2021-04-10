'''
  El Código Debe: 
    - Hacer las siguientes preguntas a un grupo de 5min personas:
        - Nombre
        - Edad
        - Estatura
        - Fruta 
    - Con estos datos sacar una lista de:
        - Quien es la más joven
        - Quien es la más vieja
        - Quien es la más alta
        - Quien es la más baja
        - Buscar quienes tienen la fruta en común
'''

# Class Info de Personas
class infoPersona:
  def __init__ (self, nombre, edad, fruta, estatura):
    self.nombre = nombre
    self.edad = edad
    self.fruta = fruta
    self.estatura = estatura

  def info (self):
    return [self.nombre, self.edad, self.fruta, self.estatura]

''' Manipulacion de datos '''

# Buscar quien tiene el dato ganador en la lista de personas 
def buscarPersona(valorGanador, indexValor):
  for i in range(numPersonas):
    if objPersona[i].info()[indexValor] == valorGanador:
      return objPersona[i].info()[0]

# Ver quien es el mas joven
def personasMenor(array, indexValor):
  array.sort() # Organiza de Menor a mayor
  print(array)
  menor = buscarPersona(array[0], indexValor)
  return menor

# Ver quien es el mas viejo
def personasMayor(array, indexValor):
  array.sort(reverse=True) # Organiza de Mayor a menor
  print(array)
  mayor = buscarPersona(array[0], indexValor)
  return mayor

# Ver si hay frutas iguales
def buscarFrutasIguales (array):
  indexEncontrado = []

''' Input de Datos '''

# Arrays de las Personas 
objPersona = []
numPersonas = 2

edadesPersonas = []
estaturaPersonas = []
frutaPersonas = []

# Entrada de Personas
for i in range(numPersonas):
  objPersona.append(infoPersona(
    nombre = input("Ingresa Tu Nombre:  "),
    edad = int(input("Ingresa Tu Edad:  ")),
    fruta = input("Ingresa Una Fruta:  "),
    estatura = float(input("Ingresa Tu Estatura en Metros:  "))
  ))

  # Datos de la Personas
  edadesPersonas.append(objPersona[i].info()[1])
  frutaPersonas.append(objPersona[i].info()[2])
  estaturaPersonas.append(objPersona[i].info()[3])
  
print(estaturaPersonas)

''' Output de Datos '''

# Imprimir Personas Menores y Mayores en Edad
print("La Persona Más Menor es:  ", personasMenor(edadesPersonas, 1))
print("La Persona Más Mayor es:  ", personasMayor(edadesPersonas, 1))

# Imprimir Personas Menores y Mayores en Estatura
print("La Persona Más Baja es:  ", personasMenor(estaturaPersonas, 3))
print("La Persona Más Alta es:  ", personasMayor(estaturaPersonas, 3))

# Imprimir Personas (Si hay) con las mismas frutas y con cuales
buscarFrutasIguales(frutaPersonas)