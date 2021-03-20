# Con python se puede asignar variables de una forma muy sencilla, solo escribiendo el nombre de la variable y su valor
number = 20
string = "Hello"

print(string + " World ", number)

# Con python no es necesario usar corchetes {} al momento de crear bloques de codigo
# Pero debemos darle un ident para que este sea reconocino como un bloque de codigo
for i in range(0, 10):
  print(string + " World", i + 1)

# Los arrays son muy utiles para tener mucha informacion en una variable
frutas = ["manzana", "pera", "banano", "kiwi", "mango", "lulo", "uvas"]

# len(), funciona para ver el largo de un array
print("Cantidad de Frutas" , len(frutas))

# varible[numero], funciona para ver una posicion del array
print("Fruta número 4", frutas[4])

# variable[- numero], funciona para ver al revez una posiscion del array
print("Ultima Fruta", frutas[-1])

# se puede usar los inputs para ingresar informacion desde la terminal de python
for i in range(4):
  nuevaFruta = input("Ingrese una nueva fruta:  ")
  print(type(nuevaFruta))
  # append(), agrega datos a el array de frutas, se puede verificar que si sean frutas o strings y demás pero necesita más codigo
  frutas.append(nuevaFruta)
  
print(frutas)