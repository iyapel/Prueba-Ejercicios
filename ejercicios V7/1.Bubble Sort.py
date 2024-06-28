def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for x in range(0, n-i-1):
            if arr[x] > arr[x+1]:
                arr[x], arr[x+1] = arr[x+1], arr[x]
                swapped = True
        if not swapped: break

# Dada una lista desordenada                
x = [9, 8, 7, 5, 4, 3, 0]

# La ordenamos utilizando bubble sort
bubble_sort(x)
print(x)
# [0, 3, 4, 5, 7, 8, 9]