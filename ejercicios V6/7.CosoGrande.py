#link con la explicacion del codigo:
#https://youtu.be/9inZCaMKeGs

condicion = 1
Mi_lista = []
while condicion == 1:
    x = int(input("Ingrese un valor a la lista: "))
    Mi_lista.append(x)
    condicion = int(input("¿Son todos los valores que desea agregar? 1-Si 2-No "))

def valor_mas_grande(Mi_lista):
    Valor_mayor = Mi_lista[0]
    for valor in Mi_lista:
         if valor > Valor_mayor:
            Valor_mayor = valor
    return Valor_mayor

print(valor_mas_grande(Mi_lista))
