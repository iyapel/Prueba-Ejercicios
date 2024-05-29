x = int(input("Cantidad de discos: "))

discos = 0
mi_lista = []
while discos < x:
    discos = discos + 1 
    mi_lista.append(discos)
    
pilar_1 = mi_lista
pilar_2 = []
pilar_3 = []

contador_de_vueltas = 0

while pilar_1 != None:
    pilar_2 = pilar_1[x - 1]
    if pilar_3[x - 1]:
        