def selection_sort(arr):
    # Traverse through all array elements
    for i in range(len(arr)):
        # Find the minimum element in the unsorted portion
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Print the array after each pass
        print(f"After pass {i + 1}: {arr}")

# Example usage
arr = [29, 10, 14, 37, 14, 5, 7]
print("Original array:", arr)
print("\nSorting process:")
selection_sort(arr)
print("\nSorted array:", arr)

"""
    Selection Sort Example:
    Original array: [29, 10, 14, 37, 14, 5, 7]

    Sorting Process:
    - Pass 1: [5, 10, 14, 37, 14, 29, 7]
    - Pass 2: [5, 7, 14, 37, 14, 29, 10]
    - Pass 3: [5, 7, 10, 37, 14, 29, 14]
    - Pass 4: [5, 7, 10, 14, 37, 29, 14]
    - Pass 5: [5, 7, 10, 14, 14, 29, 37]
    - Pass 6: [5, 7, 10, 14, 14, 29, 37]

    Time Complexity:
    Best/Average/Worst: O(n^2)
"""
