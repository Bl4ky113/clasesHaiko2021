# Made By Bl4ky113

person_dict = {
  1023: ["Martin", 15, 1.76],
  6044: ["Edwin", 15, 1.65],
  4012: ["Sebastian", 15, 1.76],
  1204: ["Camilo", 100, 1.70],
  8531: ["Pedro", 24, 1.78],
  4356: ["Juan", 100, 1.67],
  5463: ["Milena", 32, 1.70],
  1943: ["Laura", 100, 1.68],
  6789: ["Felipe", 15, 1.56],
  "viajero": ["Odiseo", 34, 1.87] 
}

keys_arr = list(person_dict.keys())

personas_menores = []
edad_menor = person_dict[keys_arr[0]][1]

personas_mayores = []
edad_mayor = person_dict[keys_arr[0]][1]

for data in person_dict.values():
  if data[1] < edad_menor:
    edad_menor = data[1]
  elif data[1] > edad_mayor:
    edad_mayor = data[1]

for id, data in person_dict.items():
  if data[1] == edad_menor:
    personas_menores.append([id, data[0]])
  elif data[1] == edad_mayor:
    personas_mayores.append([id, data[0]])

for id, persona in personas_mayores:
  print(f"La Persona {persona} con el Id {id}, tienen {edad_mayor} años")

for id, persona in personas_menores:
  print(f"La Persona {persona} con el Id {id}, tiene {edad_menor} años")