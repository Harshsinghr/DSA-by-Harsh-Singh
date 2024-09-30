#include <iostream>
#include <vector>
#include <cstdlib> // For rand()

// Utility function to swap two elements
void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

// Function to partition the array using a random pivot and return the pivot index
int partition(std::vector<int>& arr, int low, int high) {
    int pivot = arr[high]; // Choose the last element as pivot
    int i = low - 1;       // Index of smaller element

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

// Function to generate a random partition and place the pivot correctly
int randomPartition(std::vector<int>& arr, int low, int high) {
    // Generate a random index between low and high
    int randomIndex = low + rand() % (high - low + 1);

    // Swap the random element with the last element to use it as pivot
    swap(arr[randomIndex], arr[high]);

    // Call the standard partition function
    return partition(arr, low, high);
}

// Randomized Quick Sort function
void randomQuickSort(std::vector<int>& arr, int low, int high) {
    if (low < high) {
        // Partition the array and get the pivot index
        int pi = randomPartition(arr, low, high);

        // Print the array after each partition for better understanding
        std::cout << "Partition at index " << pi << ": ";
        for (int x : arr) {
            std::cout << x << " ";
        }
        std::cout << std::endl;

        // Recursively sort elements before and after partition
        randomQuickSort(arr, low, pi - 1);
        randomQuickSort(arr, pi + 1, high);
    }
}

// Helper function to print the array
void printArray(const std::vector<int>& arr) {
    for (int num : arr) {
        std::cout << num << " ";
    }
    std::cout << std::endl;
}

int main() {
    std::vector<int> arr = {10, 7, 8, 9, 1, 5};
    
    std::cout << "Original array: ";
    printArray(arr);

    std::cout << "\nSorting process:\n";
    randomQuickSort(arr, 0, arr.size() - 1);

    std::cout << "\nSorted array: ";
    printArray(arr);

    return 0;
}

/*
    Randomized Quick Sort Example:
    Original array: [10, 7, 8, 9, 1, 5]

    Sorting Process (randomized pivot each time):
    - Partition at index x: [ ... updated array after partition ... ]

    Time Complexity:
    Best/Average: O(n log n)
    Worst: O(n^2) (However, the random pivot reduces the chances significantly)
    Space Complexity: O(log n) (Due to recursion stack)

    Description:
    - Randomized Quick Sort works by randomly selecting a pivot element to reduce the chances
      of the worst-case scenario occurring (when the input array is already sorted or in reverse order).
    - The function `randomPartition` generates a random index and swaps it with the last element
      to use it as the pivot.
    - This reduces the likelihood of consistently bad pivot choices, making the average time complexity closer to O(n log n).
*/
