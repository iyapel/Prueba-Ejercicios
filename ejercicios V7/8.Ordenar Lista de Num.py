def Modificacion(arr):
    Longitud = len(arr)
    for i in range(Longitud):
        Intercambio = False
        for x in range(Longitud - i -1):
            if arr[x] < arr[x-1]:
                arr[x], arr[x-1] = arr[x-1], arr[x]
                Intercambio = True
        if not Intercambio:
            break    
    return arr

Datos = [9, 3 ,4 ,6, 5, 2, 7]
print(Modificacion(Datos))