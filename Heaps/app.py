# Build a min heap (heapify)
# Time: O(n), Space:O(1)

A = [-4,3,1,0,2,5,10,8,12,9]

import heapq

heapq.heapify(A)
# print(A)

# Heap push
heapq.heappush(A,4)
# print(A)

# Heap pop
heapq.heappop(A)
# print(A)

## Heap Sort Time: O(n log n)

def heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = []
    while(len(arr) > 0):
        popped_item = heapq.heappop(arr)
        sorted_arr.append(popped_item)
    return sorted_arr
    
arr = [-4,3,1,0,2,5,10,8,12,9]
sorted = heap_sort(arr)
print(sorted)