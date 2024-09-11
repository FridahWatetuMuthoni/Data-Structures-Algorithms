# Sorting Algorithms Notes

Here are the time complexities of the most popular sorting algorithms, commonly discussed in technical interviews:

### 1. **Bubble Sort**

- **Worst-case time complexity**: O(n²)
- **Best-case time complexity**: O(n) (if the array is already sorted)
- **Average-case time complexity**: O(n²)
- **Space complexity**: O(1) (in-place)

Bubble Sort repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

### 2. **Selection Sort**

- **Worst-case time complexity**: O(n²)
- **Best-case time complexity**: O(n²)
- **Average-case time complexity**: O(n²)
- **Space complexity**: O(1) (in-place)

Selection Sort finds the minimum element from the unsorted part of the array and swaps it with the element at the beginning of the unsorted part.

### 3. **Insertion Sort**

- **Worst-case time complexity**: O(n²)
- **Best-case time complexity**: O(n) (if the array is already sorted)
- **Average-case time complexity**: O(n²)
- **Space complexity**: O(1) (in-place)

Insertion Sort builds a sorted array by repeatedly picking elements from the unsorted array and inserting them in the correct position.

### 4. **Merge Sort**

- **Worst-case time complexity**: O(n log n)
- **Best-case time complexity**: O(n log n)
- **Average-case time complexity**: O(n log n)
- **Space complexity**: O(n) (not in-place)

Merge Sort divides the array into halves, recursively sorts the halves, and merges the sorted halves back together.

### 5. **Quick Sort**

- **Worst-case time complexity**: O(n²) (when the pivot element is the smallest or largest at each step)
- **Best-case time complexity**: O(n log n)
- **Average-case time complexity**: O(n log n)
- **Space complexity**: O(log n) (for recursion)

Quick Sort picks a "pivot" element, partitions the array into elements smaller and larger than the pivot, and recursively sorts the partitions.

### 6. **Heap Sort**

- **Worst-case time complexity**: O(n log n)
- **Best-case time complexity**: O(n log n)
- **Average-case time complexity**: O(n log n)
- **Space complexity**: O(1) (in-place)

Heap Sort builds a heap from the input data and repeatedly extracts the maximum element from the heap to build the sorted array.

### 7. **Counting Sort**

- **Worst-case time complexity**: O(n + k) (where `k` is the range of the input values)
- **Best-case time complexity**: O(n + k)
- **Average-case time complexity**: O(n + k)
- **Space complexity**: O(n + k)

Counting Sort is used when the range of input values is small, and it sorts by counting the occurrences of each value.

### 8. **Radix Sort**

- **Worst-case time complexity**: O(d(n + k)) (where `d` is the number of digits in the largest number and `k` is the range of digits)
- **Best-case time complexity**: O(d(n + k))
- **Average-case time complexity**: O(d(n + k))
- **Space complexity**: O(n + k)

Radix Sort sorts numbers by processing individual digits.

### 9. **Bucket Sort**

- **Worst-case time complexity**: O(n²) (if all elements are placed in one bucket)
- **Best-case time complexity**: O(n + k) (when elements are evenly distributed)
- **Average-case time complexity**: O(n + k)
- **Space complexity**: O(n + k)

Bucket Sort divides the array into buckets, sorts each bucket individually, and then combines the sorted buckets.

### Summary Table:

| Algorithm          | Best Case   | Average Case | Worst Case  | Space Complexity |
| ------------------ | ----------- | ------------ | ----------- | ---------------- |
| **Bubble Sort**    | O(n)        | O(n²)        | O(n²)       | O(1)             |
| **Selection Sort** | O(n²)       | O(n²)        | O(n²)       | O(1)             |
| **Insertion Sort** | O(n)        | O(n²)        | O(n²)       | O(1)             |
| **Merge Sort**     | O(n log n)  | O(n log n)   | O(n log n)  | O(n)             |
| **Quick Sort**     | O(n log n)  | O(n log n)   | O(n²)       | O(log n)         |
| **Heap Sort**      | O(n log n)  | O(n log n)   | O(n log n)  | O(1)             |
| **Counting Sort**  | O(n + k)    | O(n + k)     | O(n + k)    | O(n + k)         |
| **Radix Sort**     | O(d(n + k)) | O(d(n + k))  | O(d(n + k)) | O(n + k)         |
| **Bucket Sort**    | O(n + k)    | O(n + k)     | O(n²)       | O(n + k)         |
