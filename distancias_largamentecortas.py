
distancia_km = float(input("Ingrese una distancia en Kilometros:  "))

distancia_m = distancia_km / 1000
distancia_cm = distancia_m / 100
distancia_mili = distancia_cm / 10

print(f"La convesión de la distancia {distancia_km}km\n en Metros es {distancia_m}m,\n en Centrimetros es {distancia_cm}cm\n y en Milimetros es {distancia_mili}mm")