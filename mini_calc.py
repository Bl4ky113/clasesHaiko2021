"""
  Hacer un programa que permita que el usuario ingrese 4 numero flotantes y el programa debe imprimir los siguiente resultados: 
  1 la suma 
  2 la resta
  3 Multiplicacion
  4 Division de todos los numeros vamos a redondear el resultado a 3 decimales.
  5 Modulo del num1  %  num2
  6 Modulo de num4 %  num3
  7 num2 elevado num4 * principalmente creo que es elevarlo por el ultimo número
  8 num3 elevado al num4
  9 Con lo que vimos agregen algo más
"""

NUM_INPUTS = 4 # Only Even numbers
NUM_POSITION_NAME = ["1er", "2do", "3er", "4to", "5to", "6to", "7mo", "8vo", "9no", "10mo"]

num_arr = []
show_menu = True

for i in range(NUM_INPUTS):
  while True:
    try:
      num = float(input(f"Ingresa el {NUM_POSITION_NAME[i]} número:  "))
      num_arr.append(num)
      break
    except:
      print("Ingresa un número valido")

while True: 
  command_arr = [
    'sum',
    'sub',
    'mult',
    'div',
    'mod',
    'exp',

    'showmenu', # Must be the second last command
    'kill' # Must be the last command
  ]

  def commandString (command, operation) -> str:
    string = f" - '{command}': para ver {operation} de los números\n"
    return string

  menu = [
    "".center(40, "-"),
    "\n\nPara usar el Menu, ingresa un Commando \n\n",
    commandString('sum', 'Las Sumas'), 
    commandString('sub', 'Las Restas'), 
    commandString('mult', 'Las Multiplicaciónes'),
    commandString('div', 'Las Divisiónes'),
    commandString('mod', 'Los Módulos'),
    commandString('exp', 'Las Potenciaciónes'),
    "\n",
    " - 'showmenu': ocultar o mostrar el menu despues de cada comando\n",
    " - 'kill': para terminar de usar la calcualdora\n",
    "\n",
    "".center(40, "-")
  ]
  if show_menu:
    print("".join(menu))
  command = input(">>: ")

  if command == command_arr[0]: 
    for i in range(NUM_INPUTS):
      print(f"Suma del {NUM_POSITION_NAME[i]} número con todos lo demás números")
      for e in range(NUM_INPUTS):
        result = num_arr[i] + num_arr[e]
        print(f"{num_arr[i]} + {num_arr[e]} = {result}")
  
  elif command == command_arr[1]:
    for i in range(NUM_INPUTS):
      print(f"Resta del {NUM_POSITION_NAME[i]} número con todos los demás números")
      for e in range(NUM_INPUTS):
        result = num_arr[i] - num_arr[e]
        print(f"{num_arr[i]} - {num_arr[e]} = {result}")

  elif command == command_arr[2]:
    for i in range(NUM_INPUTS):
      print(f"Multiplicación del {NUM_POSITION_NAME[i]} número con todos los demás números")
      for e in range(NUM_INPUTS):
        result = num_arr[i] * num_arr[e]
        print(f"{num_arr[i]} * {num_arr[e]} = {result}")

  elif command == command_arr[3]:
    for i in range(NUM_INPUTS):
      print(f"División del {NUM_POSITION_NAME[i]} número con todos los demás números")
      for e in range(NUM_INPUTS):
        result = num_arr[i] / num_arr[e]
        print(f"{num_arr[i]} / {num_arr[e]} = {result:.3}")

  elif command == command_arr[4]:
    i = 0
    e = 1
    sum_i = 3
    while i <= (NUM_INPUTS):
      result = num_arr[i] % num_arr[e]
      print(f"El Módulo del {NUM_POSITION_NAME[i]} número por el {NUM_POSITION_NAME[e]} número")
      print(f"{num_arr[i]} % {num_arr[e]} = {result}")
      i += sum_i
      e = i - 1

      sum_i = 2
    else: 
      del i, e, sum_i

  elif command == command_arr[5]:
    for i in range(NUM_INPUTS):
      result = num_arr[i] ** num_arr[-1]
      print(f"La Potenciacion del {NUM_POSITION_NAME[i]} número por el Ultimo número")
      print(f"{num_arr[i]} ^ {num_arr[-1]} = {result}")

  elif command == command_arr[-2]:
    if show_menu:
      show_menu = False
    else:
      show_menu = True

  elif command == command_arr[-1]:
    print("| Bye bye |".center(20, "="))
    break