'''
   El Código debe:
   -- Identificar valores Repetidos en un Array:
      - Dejar solo uno de estos valores
      - Eliminar los valores restantes
'''

numeros = [2, 3, 3, 3, 4, 4]

valoresIguales = []

for i in range(len(numeros)):
   if numeros.count(numeros[i]) > 1:
      if [numeros.count(numeros[i]), numeros[i]] not in valoresIguales:
            valoresIguales.append([numeros.count(numeros[i]), numeros[i]])

print(numeros)
print(valoresIguales)

for i in range(len(valoresIguales)):
   for e in range(valoresIguales[i][0] - 1):
      numeros.pop(numeros.index(valoresIguales[i][1]))

print(numeros)