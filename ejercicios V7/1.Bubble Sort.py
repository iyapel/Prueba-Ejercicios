def bubble_sort(arreglo):
    n = len(arreglo)
    for i in range(n):
        swapped = False
        for x in range(0, n-i-1):
            if arreglo[x] > arreglo[x+1]:
                arreglo[x], arreglo[x+1] = arreglo[x+1], arreglo[x]
                swapped = True
        if not swapped: break
               
x = [9, 8, 7, 5, 4, 3, 0]

bubble_sort(x)
print(x)