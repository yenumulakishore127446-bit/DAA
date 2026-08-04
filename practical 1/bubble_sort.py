# Bubble Sort Program

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n - 1):

        # Flag to optimize if the array is already sorted
        swapped = False

        # Last i elements are already in place
        for j in range(n - i - 1):

            # Swap if the element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swapping occurred, array is sorted
        if not swapped:
            break

    return arr

# Driver Code
numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original Array:", numbers)

bubble_sort(numbers)

print("Sorted Array:", numbers)
