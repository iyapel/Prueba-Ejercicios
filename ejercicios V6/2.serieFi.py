#Link de la explicacion del codigo:
#https://youtu.be/zPS6R1DCMbI

Valor_1 = 0

Valor_2 = 1

Auxiliar = 0

Rango = int(input("Ingrese el número de valores que desea ver: "))

for i in range(Rango +1):
    
    Auxiliar = Valor_1 + Valor_2
    
    Valor_1 = Valor_2 
    
    Valor_2 = Auxiliar
    
    print("vuelta", i, "numero ", Auxiliar)

