#link con la explicacion del codigo:
#https://youtu.be/Sg9P7vB3Ulw

x = int(input("Cantidad de discos: "))

pilar_1 = list(range(x, 0, -1))
pilar_2 = []
pilar_3 = []

def imprimir_pilares(cont):
    print("Pilar 1:", pilar_1)
    print("Pilar 2:", pilar_2)
    print("Pilar 3:", pilar_3)
    print("Movimientos:", cont)

def resolver_torres(n, origen, auxiliar, destino, cont):
    if n == 1:
        destino.append(origen.pop())
        imprimir_pilares(cont)
        cont += 1
    else:
        cont = resolver_torres(n-1, origen, destino, auxiliar, cont)
        
        cont = resolver_torres(1, origen, auxiliar, destino, cont)
        
        cont = resolver_torres(n-1, auxiliar, origen, destino, cont)
    
    return cont

resolver_torres(x, pilar_1, pilar_2, pilar_3, 0)
