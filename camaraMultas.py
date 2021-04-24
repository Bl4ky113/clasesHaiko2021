'''
  Codigo de Cámara Multas
  Debe hacer:
    - Ingresar varios carros:
      - Distancia entre ambas cámaras
      - Velocidad maxima de la calle
      - El tiempo que se demoro el auto en pasar de una a otra cámara
      - Placa del Carro
    - Determinar cuales de estos se merecen multa, curso & ok
'''

''' Clase Carros ''' 
class infoCarros:
  def __init__ (self, tiempoRecorrido, placa):
    self.tiempoRecorrido = tiempoRecorrido
    self.placa = placa

  def info (self):
    return [self.tiempoRecorrido, self.placa]


''' Intput de Datos '''

def verificarNumLogico(mensaje):
  while True:
    var = input(mensaje)
    try: 
      var = float(var)
    except ValueError: 
      print(var, "No es una Distancia, velocidad o tiempo lógico")
    else: 
      if var > 0:
        return var
      else:
        return "ERROR"


distanciaCamaras = verificarNumLogico("Distancia entre Cámaras: ") # (m) Metros
velocidadMax = verificarNumLogico("Velocidad Máxima: ") # (km/h) KiloMetros / Hora
condicionalError = distanciaCamaras == "ERROR" or velocidadMax == "ERROR"

arrCarros = []
distanciasCarros = []
placasCarros = []
cantidadCarros = 2

for i in range(cantidadCarros):
  arrCarros.append(infoCarros(
    tiempoRecorrido = verificarNumLogico(""),
    placa = input("")
  ))

  distanciasCarros.append(arrCarros[i].info()[0])
  placasCarros.append(arrCarros[i].info()[1])
  print(arrCarros[i].info())

if condicionalError:
  print("ERROR")

else: 
  """ velocidadAuto = distanciaCamaras / convercionSegundos()

  if velocidadAuto >= (velocidadMax * 1.2):
    print("Multa")

  elif velocidadAuto < (velocidadMax * 1.2) and velocidadAuto > velocidadMax:
    print("Curso de Sensibilización")

  elif velocidadAuto <= velocidadMax: 
    print("Ok")
 """