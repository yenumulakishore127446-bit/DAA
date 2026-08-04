# Quick Sort Program

def quick_sort(arr, low, high):
    if low < high:

        # Find the partition index
        pi = partition(arr, low, high)

        # Sort elements before and after partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def partition(arr, low, high):
    # Choose the last element as pivot
    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # Swap elements
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


# Driver Code
numbers = [10, 7, 8, 9, 1, 5]

print("Original Array:", numbers)

quick_sort(numbers, 0, len(numbers) - 1)

print("Sorted Array:", numbers)
