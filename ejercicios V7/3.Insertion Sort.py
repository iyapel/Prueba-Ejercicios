def insertion_sort(lista):

  for i in range(1, len(lista)):
    valor_actual = lista[i]
    x = i - 1

    while x >= 0 and lista[x] > valor_actual:
      lista[x + 1] = lista[x]
      x = x - 1

    lista[x + 1] = valor_actual

  return lista

lista_desordenada = []
lista_ordenada = insertion_sort(lista_desordenada)
condicion = 1
Valor = 0
while condicion == 1:
    Valor = int(input("Ingrese un numero: "))
    lista_desordenada.append(Valor)
    condicion = int(input("Son todos los numeros que desea agregar? 1-No 2-Si "))

print(f"Lista desordenada: {lista_desordenada}")
print(f"Lista ordenada: {lista_ordenada}")