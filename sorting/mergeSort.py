def merge_sort(arr, level=0):
    indent = "  " * level  # Used to indent print information to show levels of recursion
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, level + 1)  # Recursively sort the left half
        merge_sort(R, level + 1)  # Recursively sort the right half

        i = j = k = 0

        # Merges two sorted lists
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements in L
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copies the remaining elements in the R
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        print(f"{indent}After merging: {arr}")

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted array:", arr)
