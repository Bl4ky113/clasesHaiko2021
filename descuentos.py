"""
  Una tienda ofrece un descuento del 15% sobre el total de la compra y un
  cliente desea saber cuanto deberá pagar finalmente por su compra.
"""

compra = float(input("Ingrese el valor de la compra:  "))

descuento = compra * (1 - 0.15)

print(f"El valor de la compra es de:  {descuento}")