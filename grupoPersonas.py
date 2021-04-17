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

  Debemos agregarle como minimo 2 cosas a el código de demás
'''

# Class Info de Personas
class infoPersona:
  def __init__ (self, nombre, edad, genero, fruta, estatura, ingresoMensual, lenguajeProgramacion):
    self.nombre = nombre
    self.edad = edad
    self.genero = genero
    self.fruta = fruta
    self.estatura = estatura
    self.ingresoMensual = ingresoMensual
    self.lenguajeProgramacion = lenguajeProgramacion

  def info (self):
    return [self.nombre, self.edad, self.genero, self.fruta, self.estatura, self.ingresoMensual, self.lenguajeProgramacion]

''' Manipulacion de datos '''

# Buscar quien tiene el dato ganador en la lista de personas 
def buscarPersona(valorGanador, indexValor):
  ganadores = [] # Array de los Ganadores
  for i in range(numPersonas):
    if objPersona[i].info()[indexValor] == valorGanador:
      ganadores.append(objPersona[i].info()[0])

  return ganadores

# Ver quien es el Menor o Mayor "Algo"
def personasMenorMayor(array, indexValor, valorBuscar):
  array.sort() # Organiza de Menor a mayor
  if valorBuscar == "mayor":
    persona = buscarPersona(array[-1], indexValor)
  if valorBuscar == "menor":
    persona = buscarPersona(array[0], indexValor)
  return persona

# Ver si hay valores iguales
def buscarValoresIguales (array, indexValor, valorBuscar):
  # Ver cuantas veces se repite un valor y cual es

  numPersonasMismoValor = [] # Array con [Numero de personas con el valor, valor]
  for i in range(numPersonas):
    if array.count(array[i]) > 1: # No ingresar el valor si no hay mas de persona con el
      if [array.count(array[i]), array[i]] not in numPersonasMismoValor:
        numPersonasMismoValor.append([array.count(array[i]), array[i]])

  # Obtener quienes los integran los grupos

  personasMismoValor = [] # Matriz con los grupos y las personas de ese grupo
  for i in range(len(numPersonasMismoValor)):
    personasMismoValor.append([numPersonasMismoValor[i][1]])
    for e in range(numPersonas):
      if objPersona[e].info()[indexValor] == numPersonasMismoValor[i][1]:
        personasMismoValor[i].append(objPersona[e].info()[0])
  
  # Organizar los datos para su salida
  if numPersonasMismoValor != []:
    mensajeSalida = [] # Array con los mensajes de todos los grupos
    for i in range(len(numPersonasMismoValor)):
      mensajeGrupo =  "Hay personas que comparten " + valorBuscar + " cómo el o la " + personasMismoValor[i][0] + ":   "
      personasGrupo = [] # Array que tiene las personas en el grupo
      for e in range(len(personasMismoValor[i]) - 1):
        personasGrupo.append(personasMismoValor[i][e + 1])
      mensajeSalida.append(mensajeGrupo + bonitosArrays(personasGrupo))
    
    # Imprimir los datos con su mensaje
    for i in range(len(mensajeSalida)):
      print(mensajeSalida[i])

  else:
    mensajeSalida = "No hay personas que compartan " + valorBuscar + "\n"
    # Imprimir los datos con su mensaje
    print(mensajeSalida)
'''
  for i in range(numPersonas):
    print(i, " i")
    for e in range(numPersonas):
      print(e, " e")
      condicional_1 = objPersona[i].info()[indexValor] == objPersona[e].info()[indexValor]
      condicional_2 = objPersona[i] != objPersona[e]
      # Verificar si la Persona tiene el mismo valor que otra Persona y que esta no sea ella misma
      if condicional_1 and condicional_2:
        numPersonasMismoValor += 1
        print(numPersonasMismoValor, "Personas")
'''
  
# Embellecer los arrays de salida
# Funciona para Pasar de [Persona1, Persona2, Persona3] a un formato más legible como Persona1, Persona2 y Persona3

def bonitosArrays (array):
  if array != [] and type(array) == type([]): # Verificar que la entrada de la funcion sea un Array
    if len(array) > 1:
      arrayBonito = "" # Resultado del array ya bonito
      for i in range(len(array) - 1):
        if i == len(array) - 2:
          arrayBonito += str(array[i]) + " "  # No Agregar coma para la ultima persona
        else:
          arrayBonito += str(array[i]) + ", " # Agregar las primeras personas con una coma para la siguiente persona

      arrayBonito += "y " + str(array[-1]) # Agregar la ultima persona, con un & o Y al inicio
      return arrayBonito
    else:
      return array[0]
  else: # Si no es un array, pa la basura
    return False

''' Input de Datos '''

# Arrays de las Personas 
objPersona = []
numPersonas = 5

edadesPersonas = []
generosPersonas = []
frutaPersonas = []
estaturaPersonas = []
ingresoPersonas = []
lenguajePersonas = []

def verificarNum(mensaje, tipoVar):
  while True:
    numVar = input(mensaje)
    try:
      if tipoVar == "int":
        numVar = int(numVar)
      elif tipoVar == "float":
        numVar = float(numVar)

    except ValueError:
      print(numVar, "No es un Valor númerico, por favor entre un valor númerico")
    else:
      return numVar

# Entrada de Personas
for i in range(numPersonas):
  # Eliminado Entrada de Inputs para Mejor comprension de la terminal
  objPersona.append(infoPersona(
    nombre = input("Name: ").capitalize(),
    edad = verificarNum("Age: ", "int"),
    genero = input("Gender: ").capitalize(),
    fruta = input("Fruit: ").capitalize(),
    estatura = verificarNum("Height: ", "float"),
    ingresoMensual = verificarNum("Mensual Income: ", "float"),
    lenguajeProgramacion = input("Programming Lenguage: ").capitalize()
  ))

  # Datos de la Personas
  edadesPersonas.append(objPersona[i].info()[1])
  generosPersonas.append(objPersona[i].info()[2])
  frutaPersonas.append(objPersona[i].info()[3])
  estaturaPersonas.append(objPersona[i].info()[4])
  ingresoPersonas.append(objPersona[i].info()[5])
  lenguajePersonas.append(objPersona[i].info()[6])

''' Output de Datos '''

# Imprimir Personas Menores y Mayores en Edad
print("La Persona Más Menor es:  ", bonitosArrays(personasMenorMayor(edadesPersonas, 1, "menor")))
print("La Persona Más Mayor es:  ", bonitosArrays(personasMenorMayor(edadesPersonas, 1, "mayor")))

# Imprimir Personas (si hay) con el mismo genero
buscarValoresIguales(generosPersonas, 2, "generos")

# Imprimir Personas (Si hay) con las mismas frutas
buscarValoresIguales(frutaPersonas, 3, "frutas")

# Imprimir Personas Menores y Mayores en Estatura
print("La Persona Más Baja es:  ", bonitosArrays(personasMenorMayor(estaturaPersonas, 4, "menor")))
print("La Persona Más Alta es:  ", bonitosArrays(personasMenorMayor(estaturaPersonas, 4, "mayor")))

# Imprimir Personas con Ingresos Menores y Ingresos Mayores
print("La Persona con el Ingreso Más Bajo es:  ", bonitosArrays(personasMenorMayor(ingresoPersonas, 5, "menor")))
print("La Persona con el Ingreso Más Alto es:  ", bonitosArrays(personasMenorMayor(ingresoPersonas, 5, "mayor")))

# Imprimir Personas (Si hay) con el mismo lenguaje de programacion
buscarValoresIguales(lenguajePersonas, 6, "Lenguajes de Programación")