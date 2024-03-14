def bubble_sort(arr):
    n = len(arr)
    print(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    return arr

list = [6, 5, 7, 8, 9, 3, 4]
bubble_sort(list)
print("Sorted array:", list)