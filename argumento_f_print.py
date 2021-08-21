f = "perro"

print(f)

print(f"valor: {f}")

try:
	print(f"{f}", f, f"{perro}")
except:
	print("Upa, se daño")

# Puede el label del input() usar el argumento f?

try:
	perro = input(f"Ingrese {f}:  ")
except:
	print("Paila no puede") # Sí, sí puede

try:
	gato = input(f"{f}", f, f"{pajaro}:  ")
except:
	print("Paila tampoco pudo")

# Sirve cómo una funcion o cómo?
numero = 15

print(f"{numero}" + " gatos")

print(f"numero" + 5)
