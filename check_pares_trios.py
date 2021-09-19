from random import sample
baraja = []

numeros = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a') #Tuplas
palos = ('Corazon', 'Picas', 'Diamentes', 'Treboles')

def revisar_cartas(cartas):
    resultado = {}
    for carta in cartas:
        if carta[0] not in resultado:
            resultado[carta[0]] = [1, []]
        else:
            resultado[carta[0]][0] += 1
        
        resultado[carta[0]][1].append(carta[1])
    return resultado

def contar_pares_trios(diccionario):
    contador = {}

    for llave, valor in diccionario.items():
        contador_pares = 0
        contador_trios = 0
        contador[llave] = {}

        if (valor[0] % 2) == 0:
            contador_pares = valor[0] / 2
        elif (valor[0] % 3) == 0:
            contador_trios = valor[0] / 3
    
        contador[llave]["pares"] = contador_pares
        contador[llave]["trios"] = contador_trios

    return contador

for palo in palos:
    for numero in numeros:
        baraja.append([numero, palo])

for veces in range(50):
    cartas_elegidas = sample(baraja, 5)
    resultado_cartas = revisar_cartas(cartas_elegidas)

    resultado = contar_pares_trios(resultado_cartas)

    print(f"\nEn la mano {cartas_elegidas}")

    for llave in resultado.keys():
        # resultado.keys() == resultado_cartas.keys() ?
        value = resultado_cartas[llave]

        if value[0] > 1:
            print(f"El número: {llave} tiene")
            print(f"{resultado[llave]['pares']} pares y {resultado[llave]['trios']} trios")
            print(f"Con las cartas: {value[1]}")

    