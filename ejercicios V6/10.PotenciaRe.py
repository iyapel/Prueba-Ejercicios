def Potencias(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif a == 0:
        return 0
    else:
        return a * Potencias(a, b - 1)
        
a = int(input("El valor que se quiere elevar: "))
b = int(input("cuantas veces quiere elevar el valor: "))

print(Potencias(a, b))

