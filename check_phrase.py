"""
  Contar cuantas veces se repite cada letra en una frase que el usuario ingrese
"""

count_letters = {}

phrase = input("Ingresa tu Frase favorita:  ")
phrase_arr = phrase.split(" ")

for word in phrase_arr:
  for char in word:
    if char not in count_letters:
      count_letters[f"{char}"] = 1
    else:
      count_letters[f"{char}"] += 1

print("La Frase:".center(5, " "))
print("|||".center(12 + len(phrase), "="), "\n")
print("'".center(5, " "), f"{phrase}", "'".center(5, " "), "\n")
print("|||".center(12 + len(phrase), "="))

for letter in count_letters:
  print(f"Tiene {count_letters.get(letter)} {letter}")