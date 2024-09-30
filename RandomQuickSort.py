import random

# Function to partition the array and return the partition index
def partition(arr, low, high):
    pivot = arr[high]  # Choose the last element as the pivot
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap pivot into the correct position
    return i + 1

# Function to generate a random partition
def random_partition(arr, low, high):
    random_index = random.randint(low, high)  # Generate a random index
    arr[random_index], arr[high] = arr[high], arr[random_index]  # Swap the random element with the last element
    return partition(arr, low, high)

# Randomized Quick Sort function
def random_quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pi = random_partition(arr, low, high)

        # Print the array after each partition for better understanding
        print(f"Partition at index {pi}: {arr}")

        # Recursively sort elements before and after the partition
        random_quick_sort(arr, low, pi - 1)
        random_quick_sort(arr, pi + 1, high)

# Example usage
arr = [10, 7, 8, 9, 1, 5]

print("Original array:", arr)
print("\nSorting process:")
random_quick_sort(arr, 0, len(arr) - 1)

print("\nSorted array:", arr)

"""
    Randomized Quick Sort Example:
    Original array: [10, 7, 8, 9, 1, 5]

    Sorting Process (with random pivots):
    - Partition at index x: [... updated array after each partition ...]

    Time Complexity:
    Best/Average: O(n log n)
    Worst: O(n^2) (Random pivot selection greatly reduces the chances of worst-case scenario)
    Space Complexity: O(log n) (Due to recursion stack)

    Description:
    - Randomized Quick Sort works by randomly selecting a pivot element to reduce the chances
      of getting the worst-case time complexity.
    - The random pivot reduces the risk of consistently poor pivot choices, helping maintain
      an average time complexity of O(n log n).
"""
