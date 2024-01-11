# Milagros Álvarez Cisterna

# El programa tendra la finalidad de contar los votos de las elecciones de un
# centro de estudiantes. Luego calculará los porcentajes, mostrará el ganador y
# un listado ordenado de mayor a menor.

# Función para ingresar los votos
def ingresar_votos():
    voto = 0
    votos = [0, 0, 0, 0, 0, 0]
    while voto != 6:
        voto = input(
            "¿A quien vota? (1 - Verde 2 - Amarillo 3 - Rojo 4 - Voto en blanco 5 - Voto nulo 6 - terminar)")
        voto = int(voto)
        if voto == 6:
            break
        votos[voto] = votos[voto] + 1

    return votos

# Función para calcular los porcentajes de votos
def calcular_porcentaje(votos):
    total = 0
    porcentajes = [0, 0, 0, 0, 0, 0]
    for cantidad in votos:
        total = total + cantidad
    for x in range(1, len(votos)):
        porcentajes[x] = votos[x] / total * 100
    return porcentajes

# Función para obtener el índice del ganador
def obtener_ganador(votos):
    mayor = votos[0]
    indice = 0
    for x in range(1, len(votos)):
        if votos[x] > mayor:
            mayor = votos[x]
            indice = x
    return indice

# Función para ordenar los resultados de mayor a menor
def ordenar_resultados(porcentajes):
    resultados = []
    for x in range(1, len(porcentajes)):
        resultados.append((x, porcentajes[x]))

    for k in range(len(resultados) - 1):
        for x in range(len(resultados) - 1 - k):
            if resultados[x][1] < resultados[x + 1][1]:
                aux = resultados[x]
                resultados[x] = resultados[x + 1]
                resultados[x + 1] = aux
    return resultados



# Etiquetas para los diferentes candidatos y opciones de voto
etiquetas = ["", "Verde", "Amarillo", "Rojo", "Voto en blanco", "Voto nulo"]
# Llamada a la función para ingresar los votos
votos = ingresar_votos()

# Imprimir resultados de la elección
print("Resultados de la elección: ")
for x in range(1, len(votos)):
    print(etiquetas[x], "sacó ", votos[x], "votos.")

# Calcular y mostrar los porcentajes de la elección
print("\nPorcentajes de la elección: ")

porcentajes = calcular_porcentaje(votos)
for x in range(1, len(porcentajes)):
    print(etiquetas[x], "tiene el ", porcentajes[x], "%")
# Obtener y mostrar el ganador de la elección
mayor = obtener_ganador(votos)
print("\nEl ganador es ", etiquetas[mayor])

# Mostrar resultados ordenados de mayor a menor
print("\nResultados ordenados: ")

resultados_ordenados = ordenar_resultados(porcentajes)
for x in range(1, len(resultados_ordenados)):
    print(etiquetas[resultados_ordenados[x][0]], "tiene el ", resultados_ordenados[x][1], "%")