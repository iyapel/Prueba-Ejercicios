x = int(input("Cantidad de discos: "))

# Inicialización de los pilares
pilar_1 = list(range(x, 0, -1))
pilar_2 = []
pilar_3 = []

# Función para imprimir el estado de los pilares
def imprimir_pilares(cont):
    print("Pilar 1:", pilar_1)
    print("Pilar 2:", pilar_2)
    print("Pilar 3:", pilar_3)
    print("Movimientos:", cont)

# Función recursiva para resolver el problema
def resolver_torres(n, origen, auxiliar, destino, cont):
    if n == 1:
        # Moviendo el disco superior de origen a destino
        destino.append(origen.pop())
        imprimir_pilares(cont)
        cont += 1
    else:
        # Moviendo n-1 discos de origen a auxiliar usando destino como auxiliar
        cont = resolver_torres(n-1, origen, destino, auxiliar, cont)
        # Moviendo el disco restante de origen a destino
        cont = resolver_torres(1, origen, auxiliar, destino, cont)
        # Moviendo n-1 discos de auxiliar a destino usando origen como auxiliar
        cont = resolver_torres(n-1, auxiliar, origen, destino, cont)
    return cont

# Llamada inicial a la función
resolver_torres(x, pilar_1, pilar_2, pilar_3, 0)