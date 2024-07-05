def Resuelve(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = []
condicion_1 = int(input("¿Cuántas cadenas de texto desea agregar? "))

for i in range(condicion_1):
    valor = input("Ingrese una cadena de texto: ")
    arr.append(valor)
    
resultado = Resuelve(arr)

for cadena in resultado:
    print(cadena)