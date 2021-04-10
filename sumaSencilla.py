
# Array del las Sumas 
resultados = []

def suma ():
 x = int(input("Ingrese un Número:  "))
 y = int(input("Ingrese un Número:  "))
 return x + y

# Entrada de los Inputs
for i in range(5):
 resultados.append(suma())
 print("El resultado de su suma es:  ", resultados[i])

# Print de los Inputs
print("El resultado de todas las sumas es:  ", resultados)

