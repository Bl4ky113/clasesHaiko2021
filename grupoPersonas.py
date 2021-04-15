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

  Debemos agregarle como minimo 2 cosas a el códido de demás
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
      mensajeGrupo =  "Hay personas que comparten " + valorBuscar + " cómo el o la " + personasMismoValor[i][0] + " "
      personasGrupo = [] # Array que tiene las personas en el grupo
      for e in range(len(personasMismoValor[i]) - 1):
        personasGrupo.append(personasMismoValor[i][e + 1])
      mensajeSalida.append(mensajeGrupo + str(personasGrupo))
    
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
''' Input de Datos '''

# Arrays de las Personas 
objPersona = []
numPersonas = 6

edadesPersonas = []
estaturaPersonas = []
frutaPersonas = []

# Entrada de Personas
for i in range(numPersonas):
  # Eliminado Entrada de Inputs para Mejor comprension de la terminal
  objPersona.append(infoPersona(
    nombre = input(),
    edad = int(input()),
    fruta = input(),
    estatura = float(input())
  ))

  # Datos de la Personas
  edadesPersonas.append(objPersona[i].info()[1])
  frutaPersonas.append(objPersona[i].info()[2])
  estaturaPersonas.append(objPersona[i].info()[3])

''' Output de Datos '''

# Imprimir Personas Menores y Mayores en Edad
print("La Persona Más Menor es:  ", personasMenorMayor(edadesPersonas, 1, "menor"))
print("La Persona Más Mayor es:  ", personasMenorMayor(edadesPersonas, 1, "mayor"))

# Imprimir Personas Menores y Mayores en Estatura
print("La Persona Más Baja es:  ", personasMenorMayor(estaturaPersonas, 3, "menor"))
print("La Persona Más Alta es:  ", personasMenorMayor(estaturaPersonas, 3, "mayor"))

# Imprimir Personas (Si hay) con las mismas frutas y con cuales
buscarValoresIguales(frutaPersonas, 2, "frutas")