Numero = int(input("Ingrese un Numero: "))
Valores = []

for i in range(1, Numero):
    if Numero % i == 0:
        Valores.append(i)

valor_maximo = -300000

for x in Valores[:]:
    if x > valor_maximo:
        valor_maximo = x

print(valor_maximo)
print(Valores[:])
