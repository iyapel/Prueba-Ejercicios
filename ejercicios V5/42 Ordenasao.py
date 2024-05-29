print("-----Ordenamiento burbuja------")

def ordenamiento_burbuja(lista):
  n = len(lista)
  for i in range(n-1):
    for j in range(0, n-i-1):
      if lista[j] > lista[j+1]:
        lista[j], lista[j+1] = lista[j+1], lista[j]

  return lista
lista = []
cond = 1
while cond == 1:
    lista.append(int(input("Ingrese un valor ")))
    cond = int(input("Son todos los datos que quiere poner? 1-No  2-Si "))

lista_ordenada = ordenamiento_burbuja(lista)
print(lista_ordenada)
