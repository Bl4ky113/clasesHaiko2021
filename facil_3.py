""" 
   En una fábrica de computadoras se planea ofrecer a los clientes un
   descuento que dependerá del número de computadoras que compre. Si las
   computadoras son menos de cinco se les dará un 10% de descuento sobre
   el total de la compra; si el número de computadoras es mayor o igual a
   cinco pero menos de diez se le otorga un 20% de descuento; y si son 10 o
   más se les da un 40% de descuento. El precio de cada computadora es de
   $3.500.000
"""

valorPc = 3500000

for i in range(3):
   numPc = int(input("Ingrese el Número de Computadores Comprados:  "))
   valorCompra = numPc * valorPc

   if numPc < 5:
      descuento = valorCompra * 0.1

   elif numPc >=5 and numPc < 10:
      descuento = valorCompra * 0.2 
      
   else:
      descuento = valorCompra * 0.4

   totalCompra = valorCompra - descuento

   print("*****************************\n")
   print("El total de la compra es de:  ", totalCompra)
   print("\n*****************************")
