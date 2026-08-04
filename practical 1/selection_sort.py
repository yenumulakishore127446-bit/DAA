# Selection Sort Program

arr = [64, 25, 12, 22, 11]

n = len(arr)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap the minimum element with the first unsorted element
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted array:")
print(arr)
