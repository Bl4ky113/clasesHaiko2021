# Made By Bl4ky113

person_dict = {
  1023: ["Martin", 15, 1.76],
  1204: ["Camilo", 100, 1.70],
  4012: ["Sebastian", 15, 1.76],
  6044: ["Edwin", 12, 1.65],
  8531: ["Pedro", 24, 1.78],
  4356: ["Juan", 18, 1.67],
  5463: ["Milena", 32, 1.70],
  1943: ["Laura", 36, 1.68],
  6789: ["Felipe", 10, 1.56],
  "viajero": ["Odiseo", 34, 1.87] 
}

# Imprimir los contenidos de los Ids
for person_id in person_dict:
  print(person_dict[person_id])

# Imprimir los Ids y los contenidos con .items()
for person_id, person_data in person_dict.items():
  print(f"El Id: {person_id} tiene: {person_data}")