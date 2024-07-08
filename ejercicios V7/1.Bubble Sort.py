def bubble_sort(arr):  
    longitud = len(arr)  
    for i in range(longitud - 1): 
        intercambiado = False 
        for x in range(longitud - i - 1): 
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
                intercambiado = True  
        if not intercambiado:  
            break  
    return arr  

lista = [6, 5, 3, 2, 1, 9, 7, 4, 8]

lista_ordenada = bubble_sort(lista)  
print(lista_ordenada)  