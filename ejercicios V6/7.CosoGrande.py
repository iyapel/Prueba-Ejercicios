#link con la explicacion del codigo:
#https://youtu.be/9inZCaMKeGs

condicion = 1
Mi_lista = []
while condicion == 1:
    x = int(input("Ingrese un valor a la lista: "))
    Mi_lista.append(x)
    condicion = int(input("¿Son todos los valores que desea agregar? 1-Si 2-No "))

def valor_mas_grande(Mi_lista, Ubicacion):
    if Ubicacion == 0:
        return Mi_lista[0]
    else:
        valor_grande = valor_mas_grande(Mi_lista, Ubicacion - 1)
        if Mi_lista[Ubicacion] > valor_grande:
            valor_grande = Mi_lista[Ubicacion]
        return valor_grande

Ubicacion = len(Mi_lista)
valor_maximo = valor_mas_grande(Mi_lista, Ubicacion - 1)
print(f"El valor máximo en la lista es: {valor_maximo}")