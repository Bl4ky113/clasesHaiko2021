
VOCALES = ['a', 'e', 'i', 'o', 'u']

arr_palabras = []
arr_tieneVocal = []
arr_numVocales = []
arr_vocalesPalabras = []

str_tieneVocal = "" # True => Si || false => No
palabra = input("Ingresa la primera palabra: ")
tieneVocal = False
numVocales = 0
vocalesPalabras = ""

while palabra != "fin":
  tieneVocal = False
  numVocales = 0
  vocalesPalabras = ""

  arr_palabras.append(palabra)

  for i in palabra:
    if i in VOCALES:
      tieneVocal = True
      numVocales += 1
      vocalesPalabras += i
    else:
      if tieneVocal != True:
        tieneVocal = False

  arr_tieneVocal.append(tieneVocal)
  arr_numVocales.append(numVocales)
  arr_vocalesPalabras.append(vocalesPalabras);
  palabra = input("Ingresa una palabra: ")


for i in range(len(arr_palabras)):
  if arr_tieneVocal[i] == True:
    str_tieneVocal = "Sí"
  else:
    str_tieneVocal = "No"

  print(f"La Palabra '{arr_palabras[i]}' {str_tieneVocal} tiene vocales.")
  print(f"Tiene {arr_numVocales[i]} vocales. Y estas son: {arr_vocalesPalabras[i]}")