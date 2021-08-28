"""
  Sumar los arrays con index inversos
"""

arr_1 = [2, 4, 6, 8, 10]
arr_2 = [1, 3, 5, 7, 9]

for i in range(len(arr_1)):
  print(f"{arr_1[i]} + {arr_2[(len(arr_2) - 1) - i]} = {arr_1[i] + arr_2[(len(arr_2) - 1) - i]}")