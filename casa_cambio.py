
EL_JEFE = "Bl4ky113"

DOLAR = 3870.9
EURO = 4529.09

print(f"Bienvenidos a la Casa de cambio de {EL_JEFE}")
print(f"El Dolar esta a:  {DOLAR}\nEl Euro esta a:  {EURO}")

colombian_pesos = float(input("Ingrese la cantidad de Pesos $COP que tiene para el cambio:  "))

pesos_dolar = colombian_pesos / DOLAR
pesos_euro = colombian_pesos / EURO

print(f"${colombian_pesos} quivalen a ${pesos_dolar} Dolares")
print(f"${colombian_pesos} quivalen a ${pesos_euro} Euros")