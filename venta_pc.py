"""
  Imaginen que uds tienen un empresa que se dedica a la comercializacion de computadores, 
  el programa debe permitir ingresar el valor de compra de un computador y al final debe 
  imprimir cual seria el precio de venta si uds quieren generar un 30%  de incremento en el 
  precio original del producto.  Tambien debe imprimir cuando uds se ganan en cada producto
"""

valor_pc = float(input("Valor del Computador Comprado:  "))

valor_venta = valor_pc * 1.30
valor_ganancia = valor_venta - valor_pc

print(f"El Precio a vender el computador es de:  {valor_venta}")
print(f"La Ganancia de la venta es de: {valor_ganancia}")