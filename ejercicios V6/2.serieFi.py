#Link de la explicacion del codigo:
#https://youtu.be/zPS6R1DCMbI

Valor_1 = 0

Valor_2 = 1

Auxiliar = 0

Rango = int(input("Ingrese el número de valores que desea ver: "))
Limitador = 0

def Resolver(Valor_1,Valor_2,Auxiliar, Rango, Limitador):
    if Limitador == Rango:
        return
    else:
        Auxiliar = Valor_1 + Valor_2
        Valor_1 = Valor_2 
        Valor_2 = Auxiliar
        
        print("vuelta", Limitador, "numero ", Auxiliar)
        
        Limitador = Limitador + 1
        
        Resolver(Valor_1,Valor_2,Auxiliar, Rango, Limitador)

Resolver(Valor_1,Valor_2,Auxiliar, Rango, Limitador)
