def Quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[-1]
        diminuto = [x for x in arr[:-1] if x <= pivote]
        grandote = [x for x in arr[:-1] if x > pivote]
        return Quick_sort(diminuto) + [pivote] + Quick_sort(grandote)

Lista = []

condicion_1 = int(input("Cuantos valores desea agregar a la lista? "))
condicion_2 = 0

while condicion_2 != condicion_1:
    Valor = int(input("Ingrese un valor: "))
    Lista.append(Valor)
    condicion_2 = condicion_2 + 1

Lista_final = Quick_sort(Lista)
print(Lista_final)