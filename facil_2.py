""" 
   En una tienda de descuento se efectúa una promoción en la cual se hace un
   descuento sobre el valor de la compra total según el color de la bolita que el
   cliente saque al pagar en caja. Si la bolita es de color blanco no se le hará
   descuento alguno, si es verde se le hará un 10% de descuento, si es amarilla un
   25%, si es azul un 50% y si es roja un 100%. Determinar la cantidad final que el
   cliente deberá pagar por su compra. se sabe que solo hay bolitas de los colores mencionados
"""

from random import randint

class compra:
   def __init__ (self, valorCompra, colorBola):
      self.valorCompra = valorCompra
      self.colorBola = colorBola

   def info (self):
      return [self.valorCompra, self.colorBola]

infoCompras = []

valorBolas = [
   0,
   0.1,
   0.25,
   0.5,
   1
]
colorBolas = [
   "Blanco",
   "Verde",
   "Amarillo",
   "Azul",
   "Rojo"
]
arrBolas = [valorBolas, colorBolas]


for i in range(6):
   infoCompras.append(compra(
      float(input("Valor de la Compra:  ")),
      randint(0, 4)
   ))

   totalCompra = infoCompras[i].info()[0] - (infoCompras[i].info()[0] * arrBolas[0][infoCompras[i].info()[1]])

   print("******************************************\n")
   print("Su Compra es de:  ", infoCompras[i].info()[0])
   print("El Color de la Bola es:  ", arrBolas[1][infoCompras[i].info()[1]])
   print("Valor total de la Compra, con descuento, es de:   ", totalCompra)
   print("\n*******************************************")