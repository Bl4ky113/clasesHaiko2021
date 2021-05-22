""" 
   El Ejercicio es:  
   Se desea determinar la cantidad de dinero que recibira un trabajor por concepto de las horas extra trabajadas en una empresa
   sabiendo que se consideran horas extras las 40h laboradas y estas 40h se pagaran por una paga definida por nosotros, de 1 a 8 horas extras 
   se pagan el doble de la paga definida y de 8 a infinito horas se pagan el triple de paga definida
"""

class infoTrabajador:
   def __init__ (self, horasTrabajadas, pagoHoras):
      self.horasTrabajadas = horasTrabajadas
      self.pagoHoras = pagoHoras

   def info (self):
      return [self.horasTrabajadas, self.pagoHoras]

""" Input de Datos """

trabajador = []

for i in range(3):
   trabajador.append(infoTrabajador(
      float(input("Horas Trabajadas:  ")),
      float(input("Pago por Hora:  ")),
   ))

for i in range(3):
   if trabajador[i].info()[0] > 40 and trabajador[i].info()[0] <= 48:
      pagaTotal = trabajador[i].info()[1] * 40
      pagaTotal += ((2 * trabajador[i].info()[1]) * (trabajador[i].info()[0] - 40))
   
   elif trabajador[i].info()[0] > 48:
      pagaTotal = trabajador[i].info()[1] * 40
      pagaTotal += (2 * trabajador[i].info()[1]) * 8
      pagaTotal += (3 * trabajador[i].info()[1]) * (trabajador[i].info()[0] - 48)

   else: 
      pagaTotal = trabajador[i].info()[0] * trabajador[i].info()[1]

   print("***********************************************\n")
   print("Trabajador N°", i + 1, " Gana:  ", pagaTotal)
   print("\n***********************************************")