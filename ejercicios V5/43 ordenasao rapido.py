print("-----Ordenacion Rapida-----")

def quicksort(lista):
  if len(lista) <= 1:
    return lista

  pivote = lista[len(lista) // 2]
  menores = [x for x in lista if x < pivote]
  mayores = [x for x in lista if x >= pivote]

  return quicksort(menores) + [pivote] + quicksort(mayores)
cond = 1
lista_desordenada = []
while cond == 1:
  lista_desordenada = [lista_desordenada.append(int(input("Ingrese un valor a la Lista ")))]
  cond = int(input("Son todos los valores que desea agregar? 1-NO 2-SI "))

try:
  lista_ordenada = quicksort(lista_desordenada)
except RecursionError:
  print("RecursionError: La profundidad máxima de recursión ha sido superada.")
  print("Prueba a aumentar el límite de recursión o usar un algoritmo no recursivo.")

else:
  print(lista_ordenada)

