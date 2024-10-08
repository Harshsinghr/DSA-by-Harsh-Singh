def merge_sort(arr):
    if len(arr) > 1:
        # Find the middle point and divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Initialize pointers for merging
        i = j = k = 0

        # Merge the two halves back into arr
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements of left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements of right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        # Print the array after each merge for better understanding
        print(f"Merged array: {arr}")

# Example usage
arr = [12, 11, 13, 5, 6, 7]

print("Original array:", arr)
print("\nSorting process:")
merge_sort(arr)

print("\nSorted array:", arr)

"""
    Merge Sort Example:
    Original array: [12, 11, 13, 5, 6, 7]

    Sorting Process:
    - After merging: [11, 12]
    - After merging: [5, 6, 7]
    - After merging: [11, 12, 13]
    - After merging: [5, 6, 7, 11, 12, 13]

    Time Complexity: O(n log n)
    Space Complexity: O(n) (Due to temporary arrays)
"""
