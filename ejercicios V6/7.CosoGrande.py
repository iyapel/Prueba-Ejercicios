cond = 1
Mi_lista = []
while cond == 1:
    x = int(input("Ingrese un valor a la lista: "))
    Mi_lista.append(x)
    cond = int(input("¿Son todos los valores que desea agregar? 1-No 2-Si "))

def valor_mas_grande(Mi_lista):
    Valor_mayor = Mi_lista[0]
    for valor in Mi_lista:
         if valor > Valor_mayor:
            Valor_mayor = valor
    return Valor_mayor

print(valor_mas_grande(Mi_lista))