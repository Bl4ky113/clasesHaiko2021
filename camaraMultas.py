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

from lineasBonitas import lineasBonitas as LB

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


distanciaCamaras = verificarNumLogico("Distancia entre Cámaras (m): ") # (m) Metros
velocidadMax = verificarNumLogico("Velocidad Máxima (km/h): ") # (km/h) KiloMetros / Hora
condicionalError = distanciaCamaras == "ERROR" or velocidadMax == "ERROR"

arrCarros = []
distanciasCarros = []
placasCarros = []
cantidadCarros = 3

for i in range(cantidadCarros):
  print(LB(100))
  print("Carro N°" + str(i + 1))
  arrCarros.append(infoCarros(
    tiempoRecorrido = verificarNumLogico("Tiempo en Recorrer Distancia (seg): "),
    placa = input("Placa del Carro: ").upper()
  ))

  distanciasCarros.append(arrCarros[i].info()[0])
  placasCarros.append(arrCarros[i].info()[1])

if condicionalError:
  print("ERROR")

else: 
  def convertirVelocidad (valor):
    valor = (valor * 1000) / 3600
    return valor

  carrosMultados = []
  carrosCursos = []
  carrosOk = []

  velocidadMax = convertirVelocidad(velocidadMax)
  print(velocidadMax)
  print(velocidadMax * 1.2)

  for i in range(cantidadCarros):
    velocidadAuto = distanciaCamaras / arrCarros[i].info()[0]
    print(str(distanciaCamaras), " / " , str(arrCarros[i].info()[0]))
    print(velocidadAuto)

    if velocidadAuto >= (velocidadMax * 1.2):
      carrosMultados.append(arrCarros[i].info()[1])

    elif velocidadAuto < (velocidadMax * 1.2) and velocidadAuto > velocidadMax:
      carrosCursos.append(arrCarros[i].info()[1])

    elif velocidadAuto <= velocidadMax: 
      carrosOk.append(arrCarros[i].info()[1])

''' Output de Datos '''
print(LB(100) + "\n")
print("Carros con Multas: ", str(carrosMultados))
print("Carros que deben ir a Cursos de Sensibilación: ", str(carrosCursos))
print("Carros ok: ", str(carrosOk))
print("\n" + LB(100))