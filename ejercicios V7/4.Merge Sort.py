def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mitad = len(arr) // 2

    mitad_izquierda = arr[:mitad]
    mitad_derecha = arr[mitad:]

    mitad_izquierda = merge_sort(mitad_izquierda)
    mitad_derecha = merge_sort(mitad_derecha)

    arr_ordenado = merge(mitad_izquierda, mitad_derecha)
    
    return arr_ordenado

def merge(izquierda, derecha):

    resultado = []
    indice_izquierda, indice_derecha = 0, 0

    while indice_izquierda < len(izquierda) and indice_derecha < len(derecha):
        if izquierda[indice_izquierda] <= derecha[indice_derecha]:
            resultado.append(izquierda[indice_izquierda])
            indice_izquierda += 1
        else:
            resultado.append(derecha[indice_derecha])
            indice_derecha += 1

    while indice_izquierda < len(izquierda):
        resultado.append(izquierda[indice_izquierda])
        indice_izquierda += 1

    while indice_derecha < len(derecha):
        resultado.append(derecha[indice_derecha])
        indice_derecha += 1
    
    return resultado

arr = []
condicion_1 = int(input("Cuantos valores desea agregar a la lista? "))
condicion_2 = 0

while condicion_2 != condicion_1:
    Valor = int(input("Ingrese un valor: "))
    arr.append(Valor)
    condicion_2 = condicion_2 + 1
    
print("Arreglo original:", arr)
    
arr_ordenado = merge_sort(arr)
print("Arreglo ordenado:", arr_ordenado)