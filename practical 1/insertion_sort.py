# Insertion Sort Program

def insertion_sort(arr):
    n = len(arr)

    # Traverse from the second element
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key at its correct position
        arr[j + 1] = key

    return arr

# Driver Code
numbers = [12, 11, 13, 5, 6]

print("Original Array:", numbers)

insertion_sort(numbers)

print("Sorted Array:", numbers)
