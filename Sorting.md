# Sorting
Sorting is the process of arranging data in a specific order (e.g., ascending or descending). It's a fundamental task in computer science used to organize data for efficient searching, manipulation, and analysis.

## Time Complexity
Time complexity measures the time taken by an algorithm to run as a function of the length of the input. It helps to understand the efficiency of an algorithm, particularly when the size of the input grows.

## Space Complexity
Space complexity measures the amount of extra memory an algorithm uses as a function of the length of the input. It shows how efficiently an algorithm manages memory.

## Common Sorting Algorithms
Below are the sorting algorithms you've mentioned, along with their time and space complexities:
 
### Bubble Sort
- **Time Complexity**: Best - O(n), Average/Worst - O(n²)
- **Space Complexity**: O(1)
- Simple but inefficient. Works well for small datasets or nearly sorted data.
- [C++ Code with example](https://github.com/Harshsinghr/DSA-by-Harsh-Singh/blob/main/BubbleSort.cpp)
- [Python Code with example](https://github.com/Harshsinghr/DSA-by-Harsh-Singh/blob/main/BubbleSort.py)

### Bucket Sort
- **Time Complexity**: Best/Average - O(n + k), Worst - O(n²)
- **Space Complexity**: O(n + k)
- Used for data uniformly distributed over a range.
- [C++ Code with example](https://github.com/Harshsinghr/DSA-by-Harsh-Singh/blob/main/BucketSort.cpp)

### Counting Sort
- **Time Complexity**: O(n + k)
- **Space Complexity**: O(k)
- Efficient for data with limited range values (integers).
- [C++ Code with example](https://github.com/Harshsinghr/DSA-by-Harsh-Singh/blob/main/CountingSort.cpp)

### Heap Sort 
- **Time Complexity**: Best/Average/Worst - O(n log n)
- **Space Complexity**: O(1)
- Uses a heap data structure. Not stable but has good performance.
- [(C++ Code with example)](https://github.com/Harshsinghr/DSA-by-Harsh-Singh/blob/main/HeapSort.cpp)
- [Python Code with example](https://github.com/Harshsinghr/DSA-by-Harsh-Singh/blob/main/HeapSort.py)

### Insertion Sort
- **Time Complexity**: Best - O(n), Average/Worst - O(n²)
- **Space Complexity**: O(1)
- Works well for small or nearly sorted datasets.
- [(C++ Code with example)](https://github.com/Harshsinghr/DSA-by-Harsh-Singh/blob/main/InsertionSort.cpp)
- [Python Code with example](https://github.com/Harshsinghr/DSA-by-Harsh-Singh/blob/main/InsertionSort.py)

### Merge Sort
- **Time Complexity**: O(n log n)
- **Space Complexity**: O(n)
- Divides and conquers. Stable and efficient for large datasets.
- [(C++ Code with example)](https://github.com/Harshsinghr/DSA-by-Harsh-Singh/blob/main/MergeSort.cpp)
- [Python Code with example](https://github.com/Harshsinghr/DSA-by-Harsh-Singh/blob/main/MergeSort.py)

### Quick Sort
- **Time Complexity**: Best/Average - O(n log n), Worst - O(n²)
- **Space Complexity**: O(log n)
- Efficient in practice but can degrade with poor pivot selection.
- [(C++ Code with example)](https://github.com/Harshsinghr/DSA-by-Harsh-Singh/blob/main/QuickSort.cpp)
- [Python Code with example](https://github.com/Harshsinghr/DSA-by-Harsh-Singh/blob/main/QuickSort.py)

### Random Quick Sort
- **Time Complexity:** Best/Average: O(n log n), Worst: O(n^2)(Random pivot selection greatly reduces the chances of worst-case scenario)
- **Space Complexity:** O(log n) (Due to recursion stack)
- [Python Code with example](https://github.com/Harshsinghr/DSA-by-Harsh-Singh/blob/main/RandomQuickSort.py)
  
### Radix Sort
- **Time Complexity**: O(nk)
- **Space Complexity**: O(n + k)
- Works for integers, based on digit-by-digit sorting.
- [(C++ Code with example)](https://github.com/Harshsinghr/DSA-by-Harsh-Singh/blob/main/RadixSort.cpp)

### Selection Sort
- **Time Complexity**: Best/Average/Worst - O(n²)
- **Space Complexity**: O(1)
- Simple but inefficient, always takes O(n²) comparisons.
- [C++ Code with example](https://github.com/Harshsinghr/DSA-by-Harsh-Singh/blob/main/SelectionSort.cpp)
- [Python Code with example](https://github.com/Harshsinghr/DSA-by-Harsh-Singh/blob/main/SelectionSort.py)
