def selection_sort(arr):
    def sort_segment(arr, n):
        if n == 0:
            return
        max_idx = 0
        for i in range(1, n):
            if arr[i] > arr[max_idx]:
                max_idx = i
        arr[n-1], arr[max_idx] = arr[max_idx], arr[n-1]
        sort_segment(arr, n-1)
    
    if len(arr) < 2:
        return arr
    sort_segment(arr, len(arr))
    return arr

array = [64, 25, 12, 22, 11]
print("Array original:", array)
sorted_array = selection_sort(array)
print("Array ordenado:", sorted_array)