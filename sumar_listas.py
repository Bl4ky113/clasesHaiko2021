"""
  Sumar los contenidos con mismo index de 2 arrays
"""

num_1 = [1, 5, 6, 8, 10, 20, 40]
num_2 = [7, 8, 6, 7, 2, 5]
shortest_arr = []
loop = True

while loop:
  if len(num_1) == len(num_2):
    for i in range(len(num_1)):
      print(f"{num_1[i]} + {num_2[i]} = {num_1[i] + num_2[i]}")
      loop = False

  else:
    if len(num_1) > len(num_2): 
      shortest_arr = num_2
    else: 
      shortest_arr = num_1

    for i in range(abs(len(num_1) - len(num_2))):
      shortest_arr.append(0)
    
    del shortest_arr