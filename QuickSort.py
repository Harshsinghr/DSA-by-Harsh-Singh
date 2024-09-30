def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the partition index
        pi = partition(arr, low, high)

        # Print the array after each partition for better understanding
        print(f"Partition at index {pi}: {arr}")

        # Recursively sort elements before and after the partition
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

# Partition function to find the partition index
def partition(arr, low, high):
    pivot = arr[high]  # Select the last element as pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    # Swap the pivot element with the element at index i + 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Helper function to print the array
def print_array(arr):
    for num in arr:
        print(num, end=" ")
    print()

# Example usage
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)

print("Original array:", arr)
print("\nSorting process:")
quick_sort(arr, 0, n - 1)

print("\nSorted array:", arr)

"""
    Quick Sort Example:
    Original array: [10, 7, 8, 9, 1, 5]

    Sorting Process:
    - Partition at index 3: [1, 5, 7, 8, 10, 9]
    - Partition at index 1: [1, 5, 7, 8, 9, 10]
    - Partition at index 5: [1, 5, 7, 8, 9, 10]

    Time Complexity:
    Best/Average: O(n log n)
    Worst: O(n^2) (Occurs when the array is already sorted or in reverse order, without proper pivoting)
    Space Complexity: O(log n) (Due to recursion stack)
"""
