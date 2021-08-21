# Son arrays o listas de datos que podemos crear
# Sus index o posiciones inician desde 0 hasta la cantidad de datos que tenga

list = [10, 11, 12, 5, 15, 21]

# Se usa el [] para obtener los datos dentro de esta lista y dentro el index del dato

print(list[0])
print(list[2])
print(list[5])

# Se usan valores negativos para ir en la dirección inversa de los datos
# No se puede usar -0, solo -1

print(list[-1])
print(list[-3])
try: 
  print(list[-6])
except:
  print("Se pasa del largo del array")

# Se puede obtener una parte de los datos usando "Slicing", poniendo un index [1], dos puntos [1:] y otro index [1:5]
# Se va a posicionar en el 1er index y va a mostrar todos los datos entre ese y el 2do index
# O se puede dejar en blanco el 1er index y va a mostrar todos los datos desde el inicio hasta el 2do index [:3]
# O se puede dejar en blanco el 2do index y va a mostrar todos los datos desde el 1er index hasta el final [1:]

print(list[1:5])
print(list[:3])
print(list[1:])

# Existen diferentes metodos para los Arrays, los cuales nos permiten modificar, organizar, eliminar, agregar los datos y los index de estos

print(list.sort(reverse = True))
print(list.append(120))
print(list.reverse())

