#Link de la explicacion del codigo:
#https://youtu.be/asObeoHlaDQ

Numero = int(input("Ingrese un numero: "))

Valores = []

for i in range(2, Numero):
    if Numero % i == 0:
        Valores.append(i)
        
print("el minimo comun multiplo de", Numero, "es ", Valores[:])

