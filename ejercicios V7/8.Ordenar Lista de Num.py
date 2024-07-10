def Modificacion(arr):
    Longitud = len(arr)
    for i in range(Longitud):
        for x in range(Longitud - i -1):
            if arr[x] < arr[x+1]:
                arr[x], arr[x+1] = arr[x+1], arr[x]
    return arr

Datos = [9, 3 ,4 ,6, 5, 2, 8, 7]
print(Modificacion(Datos))