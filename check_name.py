""" 
  El usuario ingresa su nombre (first name and last name) y el programa retorna cuantas vocales y letras tiene 
"""

VOCALS = ('a', 'e', 'i', 'o', 'u')

full_name = input("Ingrese su Nombre Completo:  ")
arr_name = full_name.split(" ")

for name in arr_name:
  arr_letters = []
  arr_vocals = []
  num_vocals = 0
  num_letters = 0

  for char in name:
    if char.lower() in VOCALS:
      if char.lower() not in arr_vocals:
        arr_vocals.append(char)
      num_vocals += 1

    elif char.lower() not in VOCALS:
      if char.lower() not in arr_letters:
        arr_letters.append(char)
      num_letters += 1
      

  print(f"{name} tiene {num_vocals} vocales, cuales son: {arr_vocals}")
  print(f"Y tiene también {num_letters} letras, cuales son: {arr_letters}")