
# Merge Sort Program

def merge_sort(arr):
    if len(arr) > 1:

        # Find the middle of the array
        mid = len(arr) // 2

        # Divide the array into two halves
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort both halves
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements from left half
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements from right half
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Driver Code
numbers = [12, 11, 13, 5, 6, 7]

print("Original Array:", numbers)

merge_sort(numbers)

print("Sorted Array:", numbers)
