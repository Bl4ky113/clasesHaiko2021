
# Matriz 
suma = []
resta = []
multi = []
div = []
resultados = [suma, resta, multi, div]

# Funciones
def functionSuma  (num1, num2):
  resultados[0].append(num1 + num2)
  return num1 + num2

def functionResta (num1, num2):
  resultados[1].append(num1 - num2)

def functionMulti (num1, num2):
  resultados[2].append(num1 * num2)

def functionDiv (num1, num2):
  resultados[3].append(num1 / num2)

# Inputs de la Funcitons
for i in range(3):
  x = int(input("Ingresa un Número:  "))
  y = int(input("Ingresa otro Número:  "))
  functionSuma(x, y)
  print("Resultado de la Suma:  ", functionSuma(x, y))
  functionResta(x, y)
  print("Resultado de la Resta:  ", resultados[1][i])
  functionMulti(x, y)
  print("Resultado de la Multiplicacion:  ", resultados[2][i])
  functionDiv(x, y)
  print("Resultado de la Divisones:  ", resultados[3][i])


# Print de los Datos
print("Resultados de todas las Sumas: ", resultados[0])
print("Resultados de todas las Restas: ", resultados[1])
print("Resultados de todas las Multiplicaciones: ", resultados[2])
print("Resultados de todas las Divisiones: ", resultados[3])

print("TODOS los Resultados", resultados)